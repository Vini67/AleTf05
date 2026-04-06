#!/bin/bash

mkdir -p backups
docker exec TF05-db-1 mysqldump -u root -proot monitor > backups/backup.sql