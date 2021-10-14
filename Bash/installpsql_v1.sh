#!/bin/sh
pre_req(){
###   ##
sudo dnf -y update || { echo "The update command has failed"; exit 1;}
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm ||
echo "This script will install PostgreSQL."
# Disable the built-in PostgreSQL module:
sudo dnf -qy module disable postgresql ||{ echo "unable to disable postgesql"; exit 1;}
}
install(){
# Install PostgreSQL:
if [ -d /usr/pgsql-13/bin ]; then
echo "Postgres v13 is already installed on the host ..."
else
sudo dnf install -y postgresql13-server ||{ echo "failed to install postgresql13-server"; exit 1;}
fi
}
post_install(){
# Optionally initialize the database and enable automatic start:
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb ||{ echo "failed to enable postresql13-server automatic start"; exit 1;}
#Enable the "postgresql" to start at boot 
sudo systemctl enable postgresql-13 ||{ echo "failed to enable postresql13-server start from boot"; exit 1;}
#Start the postgresql service
sudo systemctl start postgresql-13 ||{ echo "failed to start postgresql13-server"; exit 1;}
echo Script Done!
}




