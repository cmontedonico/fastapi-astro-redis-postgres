# Full Stack Application with FastAPI, PostgreSQL, Redis, and Astro

This project is a full-stack application using FastAPI for the backend, PostgreSQL as the main database, Redis for caching, and Astro for the frontend.

## Project Structure

├── backend/ <- FASTAPI ->
│ ├── app/
│ │ ├── routes/
│ │ ├── models.py
│ │ ├── schemas.py
│ │ ├── database.py
│ │ └── redis_client.py
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
├── database/ <- Postgres ->
│ ├── Dockerfile
│ └── INIT.sql
├── redis/ <- Redis ->
│ ├── Dockerfile
│ └── redis.conf
├── frontend/ <- Astro / Typescript / Tailwind ->
│ ├── src/
│ ├── public/
│ ├── astro.config.mjs
│ ├── tailwind.config.cjs
│ ├── package.json
│ └── Dockerfile
├── docker-compose.yml
└── README.md

## Versions

- Python: 3.9
- FastAPI: 0.68.0
- PostgreSQL: 14
- Redis: 6.2
- Node.js: 18
- Astro: 2.3.0

## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Application

1. Clone the repository:

   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Build and start the containers:

   ```
   docker-compose up --build
   ```

3. The services will be available at:

   - Backend API: http://localhost:8000
   - Frontend: http://localhost:3000
   - PostgreSQL: localhost:5432
   - Redis: localhost:6379

4. To stop the application, use:
   ```
   docker-compose down
   ```

## Development

### Backend (FastAPI)

- The backend code is in the `Backend/` directory.
- You can edit the Python files locally, and the changes will be reflected immediately due to the volume mount and auto-reload feature of uvicorn.

### Frontend (Astro)

- The frontend code is in the `frontend/` directory.
- You can edit the Astro files locally, and the changes will be reflected immediately due to the volume mount and Astro's hot-reloading feature.

### Database

- The initial database schema is defined in `database/INIT.sql`.
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
