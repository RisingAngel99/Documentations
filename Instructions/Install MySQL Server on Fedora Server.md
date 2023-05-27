# Install MySQL Server on Fedora Server

```bash
sudo dnf install https://dev.mysql.com/get/mysql80-community-release-fc36-1.noarch.rpm

sudo dnf install mysql-community-server

sudo systemctl enable --now mysqld
```

```bash
sudo grep 'temporary password' /var/log/mysqld.log

sudo mysql_secure_installation

sudo mysql -u root -p
```

```bash
CREATE USER 'your_username'@'host_ip_addr' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'your_username'@'%';
FLUSH PRIVILEGES;
```

```
sudo rpm -e --nodeps mysql-community-libs mysql-community-common mysql-community-server
```