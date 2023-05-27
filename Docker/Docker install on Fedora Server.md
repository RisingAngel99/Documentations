# Install Docker & Portainer

In this Tutrial, I explain, how to install Docker and Portainer on a Fedora Server.

## Docker install

Requirements before installing docker:

```
sudo dnf upgrade -y
```

Now you can install docker:

```
sudo dnf install docker -y
```

You must config sytemctl, that docker is starting after any reboot:

```
sudo systemctl enable --now docker
```


That task makes sure, that the user don´t need sudo anymore for docker tasks:

```
sudo gpasswd -a administrator docker && sudo systemctl restart docker
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