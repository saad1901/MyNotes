# Docker Swarm

Docker Swarm is Docker's native clustering and orchestration tool, allowing you to manage a cluster of Docker nodes as a single virtual system.

## Architecture
- **Manager nodes:** Handle cluster management tasks (orchestration, scheduling).
- **Worker nodes:** Execute containers as instructed by managers.
- **Services:** Definitions of tasks to be run on the cluster.
- **Tasks:** Individual containers running as part of a service.

## Key Features
- High availability
- Load balancing
- Rolling updates
- Service discovery

## Common Commands
- **Initialize a swarm:**
  ```sh
  docker swarm init
  ```
- **Join a swarm:**
  ```sh
  docker swarm join --token <token> <manager_ip>:2377
  ```
- **Deploy a service:**
  ```sh
  docker service create --name myservice nginx
  ```
- **List services:**
  ```sh
  docker service ls
  ```
- **Scale a service:**
  ```sh
  docker service scale myservice=5
  ```
- **Remove a service:**
  ```sh
  docker service rm myservice
  ```

## Use Cases
- Deploying highly available applications
- Load balancing traffic across containers
- Rolling updates and zero-downtime deployments 