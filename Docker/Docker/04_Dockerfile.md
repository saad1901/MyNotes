# Dockerfile

A **Dockerfile** is a text file that contains instructions to build a Docker image. Each instruction creates a layer in the image.

## Basic Syntax
- Each instruction is written in uppercase (e.g., FROM, RUN, COPY).
- Comments start with `#`.

## Common Instructions
- **FROM:** Sets the base image (must be the first instruction).
  ```Dockerfile
  FROM ubuntu:20.04
  ```
- **LABEL:** Adds metadata to the image.
  ```Dockerfile
  LABEL maintainer="yourname@example.com"
  ```
- **RUN:** Executes commands in a new layer.
  ```Dockerfile
  RUN apt-get update && apt-get install -y python3
  ```
- **COPY:** Copies files from host to image.
  ```Dockerfile
  COPY . /app
  ```
- **ADD:** Similar to COPY but can also extract archives and fetch URLs.
- **WORKDIR:** Sets the working directory.
  ```Dockerfile
  WORKDIR /app
  ```
- **CMD:** Sets default command to run.
  ```Dockerfile
  CMD ["python3", "app.py"]
  ```
- **EXPOSE:** Documents the port the container listens on.
  ```Dockerfile
  EXPOSE 80
  ```
- **ENV:** Sets environment variables.
  ```Dockerfile
  ENV ENV_VAR=value
  ```

## Best Practices
- Use official base images.
- Minimize the number of layers.
- Combine commands with `&&` to reduce layers.
- Use `.dockerignore` to exclude unnecessary files.
- Specify exact versions for dependencies. 