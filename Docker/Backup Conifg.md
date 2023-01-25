
<!-- sudo (nano or vim) /etc/fstab  -->
172.20.1.2:/mnt/DATA/Docker_Backup /mnt/Docker_Backup  nfs      defaults    0       0


<!-- sudo (nano or vim) /etc/crontab  -->
0 3 * * * rsync -av /var/lib/docker /mnt/Docker_Backup/lib
0 3 * * * rsync -av /data /mnt/Docker_Backup/data