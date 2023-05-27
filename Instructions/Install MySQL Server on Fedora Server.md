# Install MySQL Server on Fedora Server

## Install and activate MySQL Server

```bash
sudo dnf install community-mysql-server -y

sudo systemctl enable --now mysqld
```

## Give root a password and login

```bash
sudo grep 'temporary password' /var/log/mysqld.log

sudo mysql_secure_installation

sudo mysql -u root -p
```

## Create Users and access witch the MySQL Database 

```bash
CREATE USER 'your_username'@'host_ip_addr' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'your_username'@'%';
FLUSH PRIVILEGES;
```