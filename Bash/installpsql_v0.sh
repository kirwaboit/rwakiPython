#!/bin/sh
# This script is for installing postgres 13 on linux
yes | sudo dnf update
# Install the repository RPM:
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
# Disable the built-in PostgreSQL module:
sudo dnf -qy module disable postgresql
# Install PostgreSQL:
sudo dnf install -y postgresql13-server
# Optionally initialize the database and enable automatic start:
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb
sudo systemctl enable postgresql-13
sudo systemctl start postgresql-13
echo Script Done!