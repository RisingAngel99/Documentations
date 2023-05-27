# Install Docker & Portainer

This Tutorial is explaining, how to install docker and portainer on a ubuntu server.

## Docker install

Requirements:

```
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
```

Install Docker:

```
sudo apt install docker docker.io
```

With this task, any docker commands doesn´t need `sudo` anymore:

```
sudo gpasswd -a "USER" docker && sudo systemctl restart docker
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