# Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications using a YAML file (`docker-compose.yml`).

## Why Use Docker Compose?
- Manage multi-container applications easily
- Define services, networks, and volumes in a single file
- Simplify development, testing, and deployment

## Basic Syntax
A `docker-compose.yml` file defines services, networks, and volumes:
```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
```

## Common Commands
- **Start services:**
  ```sh
  docker-compose up
  ```
- **Start in detached mode:**
  ```sh
  docker-compose up -d
  ```
- **Stop services:**
  ```sh
  docker-compose down
  ```
- **View logs:**
  ```sh
  docker-compose logs
  ```
- **List running services:**
  ```sh
  docker-compose ps
  ```

## Best Practices
- Use environment variables for configuration.
- Use named volumes for persistent data.
- Keep services loosely coupled. 