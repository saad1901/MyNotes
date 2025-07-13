# Docker Networking

Docker provides several networking options to connect containers to each other, to the host, and to external networks.

## Network Types
- **bridge:** Default network for containers on a single host. Containers can communicate with each other.
- **host:** Removes network isolation between the container and the Docker host.
- **none:** Disables networking for the container.
- **overlay:** Enables communication between containers across multiple Docker hosts (used in Swarm mode).
- **macvlan:** Assigns a MAC address to a container, making it appear as a physical device on the network.

## Common Networking Commands
- **List networks:**
  ```sh
  docker network ls
  ```
- **Inspect a network:**
  ```sh
  docker network inspect <network_name>
  ```
- **Create a network:**
  ```sh
  docker network create mynetwork
  ```
- **Connect a container to a network:**
  ```sh
  docker network connect mynetwork <container_name>
  ```
- **Disconnect a container from a network:**
  ```sh
  docker network disconnect mynetwork <container_name>
  ```

## Use Cases
- Isolate environments (dev, test, prod) using custom networks.
- Enable communication between multi-container applications.
- Expose container ports to the host or external networks using the `-p` or `-P` flags in `docker run`. 