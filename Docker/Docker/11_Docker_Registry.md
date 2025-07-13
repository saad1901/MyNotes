# Docker Registry

A Docker registry is a storage and distribution system for Docker images. It allows you to share images publicly or privately.

## Types of Registries
- **Docker Hub:** The default public registry provided by Docker.
- **Private Registry:** Self-hosted or cloud-hosted registries for private image storage.
- **Third-party Registries:** AWS ECR, Google Container Registry, GitHub Container Registry, etc.

## Common Commands
- **Login to a registry:**
  ```sh
  docker login <registry_url>
  ```
- **Tag an image for a registry:**
  ```sh
  docker tag myimage:latest myregistry.com/myimage:latest
  ```
- **Push an image:**
  ```sh
  docker push myregistry.com/myimage:latest
  ```
- **Pull an image:**
  ```sh
  docker pull myregistry.com/myimage:latest
  ```

## Running a Private Registry
- Start a local registry container:
  ```sh
  docker run -d -p 5000:5000 --name registry registry:2
  ```
- Push an image to your local registry:
  ```sh
  docker tag myimage localhost:5000/myimage
  docker push localhost:5000/myimage
  ```

## Best Practices
- Use private registries for sensitive or proprietary images.
- Regularly clean up unused images in your registry.
- Use access control and authentication for private registries. 