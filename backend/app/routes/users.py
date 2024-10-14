from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, security
from ..database import get_db
from ..redis_client import redis_client
import json

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Store user in Redis
    user_data = {
        "id": db_user.id,
        "username": db_user.username,
        "created_at": db_user.created_at.isoformat()
    }
    redis_client.set(f"user:{db_user.id}", json.dumps(user_data))
    
    return db_user

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = []
    for key in redis_client.scan_iter("user:*"):
        user_data = json.loads(redis_client.get(key))
        users.append(schemas.User(**user_data))
    
    if not users:
        users = db.query(models.User).offset(skip).limit(limit).all()
    
    return users

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # Try to get user from Redis
    user_data = redis_client.get(f"user:{user_id}")
    if user_data:
        return schemas.User(**json.loads(user_data))
    
    # If not in Redis, get from database
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Store user in Redis for future requests
    user_data = {
        "id": db_user.id,
        "username": db_user.username,
        "created_at": db_user.created_at.isoformat()
    }
    redis_client.set(f"user:{db_user.id}", json.dumps(user_data))
    
    return db_user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = user.username
    db_user.password = security.get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    
    # Update user in Redis
    user_data = {
        "id": db_user.id,
        "username": db_user.username,
        "created_at": db_user.created_at.isoformat()
    }
    redis_client.set(f"user:{db_user.id}", json.dumps(user_data))
    
    return db_user

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    
    # Remove user from Redis
    redis_client.delete(f"user:{user_id}")
    
    return db_user
