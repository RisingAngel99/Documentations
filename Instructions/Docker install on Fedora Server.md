# Install Docker & Portainer

This Tutorial is explaining, how to install docker and portainer on a fedora server.

## Docker install

Requirements:

```
sudo dnf upgrade -y
```

Now you can install docker:

```
sudo dnf install docker -y
```

Now you must start the docker service and make sure, that docker is starting by the restart:

```
sudo systemctl enable --now docker
```

With this task, any docker commands doesn´t need `sudo` anymore:

```
sudo gpasswd -a administrator docker && sudo systemctl restart docker
newgrp docker
```


## Portainer install
***

First, create a volume, whrer Portainer is saving:

```
docker volume create portainer_data
```

Now installing portainer:

```
docker run -d -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

At last you can check, if portainer is online

```
docker ps
```

And now, you can access the WebUI of Portainer with `https://ServerIP:9443`