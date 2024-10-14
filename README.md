# Full Stack Application with FastAPI, PostgreSQL, Redis, and Astro

This project is a full-stack application using FastAPI for the backend, PostgreSQL as the main database, Redis for caching, and Astro for the frontend.

## Project Structure

database/ <- Postgres, init.sql script and Dockerfile
redis/ <- Redis config and Dockerfile
backend/ <- FASTAPI PROJECT connected with Postgres and Redis, single user functionality
frontend/ <- Astro with Typescript and Tailwind
docker-compose.yml <- General project configuration

## Versions

- Python: 3.9
- FastAPI: 0.68.0
- PostgreSQL: 14
- Redis: 6.2
- Node.js: 18
- Astro: 4.16.2

## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Application

1. Clone the repository:

   ```
   gh repo clone cmontedonico/fastapi-astro-redis-postgres
   cd fastapi-astro-redis-postgres
   ```

2. Build and start the containers:

   ```
   docker-compose up --build
   ```

3. The services will be available at:

   - Backend API: http://localhost:8000
   - Frontend: http://localhost:4321
   - PostgreSQL: localhost:5432
   - Redis: localhost:6379

4. To stop the application, use:
   ```
   docker-compose down
   ```

## Development

### Backend (FastAPI)

- The backend code is in the `backend/` directory.
- You can edit the Python files locally, and the changes will be reflected immediately due to the volume mount and auto-reload feature of uvicorn.

### Frontend (Astro)

- The frontend code is in the `frontend/` directory.
- You can edit the Astro files locally, and the changes will be reflected immediately due to the volume mount and Astro's hot-reloading feature.

### Database

- The initial database schema is defined in `database/init.sql`.
- To make changes to the database schema, update this file and rebuild the containers.

### Redis

- The Redis configuration is in `redis/redis.conf`.
- To make changes to the Redis configuration, update this file and rebuild the containers.

## API Documentation

Once the application is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

(Add instructions for running tests when you implement them)

## Deployment

(Add instructions for deploying to production when you're ready to deploy)

## Contributing

(Add guidelines for contributing to the project)

## License

(Add your chosen license information)
