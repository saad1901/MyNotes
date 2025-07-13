# Basic Docker Commands

## Checking Docker Version
```sh
docker --version
```
Displays the installed Docker version.

## Working with Images
- **List images:**
  ```sh
  docker images
  ```
- **Pull an image:**
  ```sh
  docker pull ubuntu
  ```
- **Remove an image:**
  ```sh
  docker rmi ubuntu
  ```

## Working with Containers
- **List running containers:**
  ```sh
  docker ps
  ```
- **List all containers (including stopped):**
  ```sh
  docker ps -a
  ```
- **Run a container:**
  ```sh
  docker run -it ubuntu bash
  ```
- **Stop a container:**
  ```sh
  docker stop <container_id>
  ```
- **Remove a container:**
  ```sh
  docker rm <container_id>
  ```

## Viewing Logs
```sh
docker logs <container_id>
```

## Executing Commands in a Running Container
```sh
docker exec -it <container_id> bash
```

## Removing Unused Data
```sh
docker system prune
```
Removes unused data (dangling images, stopped containers, etc.). 