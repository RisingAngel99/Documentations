# 1. stop the cluster file system in /etc/pve/

```bash
systemctl stop pve-cluster
```

# 2. start it again but forcing local mode

```bash
pmxcfs -l
```

# 3. remove the cluster config

```bash
rm -f /etc/pve/cluster.conf /etc/pve/corosync.conf 
rm -f /etc/cluster/cluster.conf /etc/corosync/corosync.conf 
rm /var/lib/pve-cluster/corosync.authkey
```

# 4. stop the cluster file system again

```bash
systemctl stop pve-cluster
```

# 5. (optional) you may have to delete the lockfile of the cluster filesystem:

```bash
rm /var/lib/pve-cluster/.pmxcfs.lockfile
```

# 6. restart pve services (or reboot)

```bash
systemctl start pve-cluster
systemctl restart pvedaemon
systemctl restart pveproxy
systemctl restart pvestatd
```