# Docker Containers

A Docker container is a runnable instance of a Docker image. Containers are lightweight, portable, and isolated from each other and the host system.

## Container Lifecycle
- **Create:**
  ```sh
  docker create ubuntu
  ```
- **Start:**
  ```sh
  docker start <container_id>
  ```
- **Run (create + start):**
  ```sh
  docker run ubuntu
  ```
- **Stop:**
  ```sh
  docker stop <container_id>
  ```
- **Restart:**
  ```sh
  docker restart <container_id>
  ```
- **Remove:**
  ```sh
  docker rm <container_id>
  ```

## Inspecting Containers
- **View details:**
  ```sh
  docker inspect <container_id>
  ```
- **View logs:**
  ```sh
  docker logs <container_id>
  ```

## Copying Files To/From Containers
- **Copy to container:**
  ```sh
  docker cp file.txt <container_id>:/path/
  ```
- **Copy from container:**
  ```sh
  docker cp <container_id>:/path/file.txt ./
  ```

## Best Practices
- Use ephemeral containers (stateless, disposable).
- Use environment variables for configuration.
- Clean up unused containers regularly.
- Use health checks to monitor container status. 