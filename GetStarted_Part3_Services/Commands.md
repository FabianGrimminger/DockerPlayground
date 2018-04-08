# Executed Commands to run this docker-compose.yml

- Swarm initialisation
- The current node is the manager
```bash
docker swarm init
```

- Create Service ``myapp`` and deploy it on the swarn
```bash
docker stack deploy -c docker-compose.yml myapp
```

- View the swarm
```bash
 docker service ls
```

- Shutdown app
```bash
docker stack rm myapp
```

- Leave with the current node form the swarm
```bash
docker swarm leave --force
```