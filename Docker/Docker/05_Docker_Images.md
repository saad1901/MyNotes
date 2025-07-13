# Docker Images

Docker images are read-only templates used to create containers. They contain the application code, libraries, dependencies, and other files needed to run an application.

## Building Images
- Use a Dockerfile to define the image.
- Build an image with:
  ```sh
  docker build -t myimage:latest .
  ```
- The `-t` flag tags the image with a name and optional version.

## Listing Images
```sh
docker images
```

## Removing Images
```sh
docker rmi <image_name_or_id>
```

## Tagging Images
```sh
docker tag myimage:latest myrepo/myimage:v1.0
```

## Saving and Loading Images
- **Save an image to a tar file:**
  ```sh
  docker save -o myimage.tar myimage:latest
  ```
- **Load an image from a tar file:**
  ```sh
  docker load -i myimage.tar
  ```

## Pushing Images to Docker Hub
1. Log in to Docker Hub:
   ```sh
   docker login
   ```
2. Tag your image:
   ```sh
   docker tag myimage:latest username/myimage:latest
   ```
3. Push the image:
   ```sh
   docker push username/myimage:latest
   ```

## Pulling Images from Docker Hub
```sh
docker pull ubuntu:latest
``` 