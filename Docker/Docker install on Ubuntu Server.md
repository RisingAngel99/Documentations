# Install Docker & Portainer

In this Tutrial, I explain, how to install Docker and Portainer on a Ubuntu Server.

## Docker install

Requirements before installing docker:

```
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
```

Now you can install docker:

```
sudo apt install docker docker.io -y
```

That task makes sure, that the user don´t need sudo anymore for docker tasks:

```
sudo gpasswd -a %USER% docker && sudo systemctl restart docker
newgrp docker
```

## Portainer install
***

First create a volume for portainer himself with this command:

```
docker volume create portainer_data
```

Now insatlling Portainer:

```
docker run -d -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

Now you can check, if Portainer is online with:

```
docker ps
```

At last you can enter the Portainer WebUI with: https://%ServerIP%:9443