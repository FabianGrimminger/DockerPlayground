# Executed Commands on Part 4

- create 2 virtual machines
- there seems to be a bug with docker-machine 0.14 on windows, but after a [downgrade to version 0.13](https://github.com/docker/machine/issues/442) it works. Download the version and replace it at ``C:\Program Files\Docker\Docker\resources\bin\docker-machine.exe``
- these are Windows Powershell Commands
```bash
$ docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1
$ docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm2
```
- to get infos about the machines run
```bash
$ docker-machine ls
```

- make ``myvm1`` a swarm manager
- port 2377 is used instead 2376 as stated in the docs
```bash
$ docker-machine ssh myvm1 "docker swarm init --advertiese-addr <ip-address-myvm1>:2377"
```
- let ``myvm2`` join the swarm with the given command you get on the step bevor
```bash
$ docker-machine ssh myvm2 "docker swarm join --token <token> <ip-address-myvm2>:2377"
```
- my token looked like this: SWMTKN-1-38yabv5vrg9i2qu3fne6xuhzhlhk4iu9klc7p05ub2338l3b3a-ad1pod06wqjt4527uzwz8nehh

- view the created swarm
```bash
$ docker-machine ssh myvm1 "docker node ls"
```

- make it easer to send commands to myvm1
- view which node is your active node
```bash
$ docker-machine env myvm1

$ & "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression

$ docker-machine ls
```

- deploy your docker-compose.yml to the swarm
- it gets deployed on the swarm, but your docker-compose is still on your machine
```bash
$ docker stack deploy -c docker-compose.yml myapp
```

- view the services on the swarm
```bash
$ docker stack ps myapp
```