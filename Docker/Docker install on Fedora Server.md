# Install Docker & Portainer

## Docker install
***

Um die Docker Repo hinzuzufügen, braucht man folgenden Command:

```
sudo dnf install dnf-plugins-core
```

Der folgende Command fügt man die docker-ce repository hinzu:

```
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

Der folgende Command installiert nun Docker:

```
sudo dnf install docker-ce docker-ce-cli containerd.io -y
```

Um den Docker Service zu starten benutze folgendes:

```
sudo systemctl start docker
```


Um Docker in den Autostart von Fedora zu packen, braucht man folgenden Command:

```
sudo systemctl enable docker
```



Um den User nun der Dockergruppe hinzuzufügen, muss man folgendes eingeben:

```
sudo gpasswd -a administrator docker && sudo systemctl restart docker
newgrp docker
```


## Portainer install
***

Als erstes wird ein Volume erstellt, um die Daten von Portainer zu speichern:

```
docker volume create portainer_data
```

Nun wird Portainer Business Edition installiert:

```
docker run -d -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:latest
```

Jetzt kann man noch prüfen, ob Portainer richtig installiert wurde mit

```
docker ps
```