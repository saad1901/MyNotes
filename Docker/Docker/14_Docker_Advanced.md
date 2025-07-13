# Docker Advanced Topics

## Multi-Stage Builds
Multi-stage builds allow you to use multiple `FROM` statements in a Dockerfile to optimize image size and security.
```Dockerfile
FROM golang:1.20 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

## Advanced Networking
- **Overlay networks:** Connect containers across multiple hosts (used in Swarm).
- **Macvlan networks:** Assign MAC addresses to containers for direct network access.
- **Network plugins:** Extend Docker networking with third-party solutions.

## Troubleshooting
- **View container logs:**
  ```sh
  docker logs <container_id>
  ```
- **Inspect containers and images:**
  ```sh
  docker inspect <name_or_id>
  ```
- **Check resource usage:**
  ```sh
  docker stats
  ```
- **Debug with an interactive shell:**
  ```sh
  docker exec -it <container_id> sh
  ```
- **Clean up unused resources:**
  ```sh
  docker system prune
  ```

## Monitoring and Logging
- Use tools like Prometheus, Grafana, and ELK stack for monitoring and logging Docker environments. 