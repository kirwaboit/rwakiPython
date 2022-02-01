# Welcome to Docker!
---
Docker is a tool used to compartmentalize
## Table of Contents
- [1.TODO](#1-todo)
    - [1.1 Use cases](#11-usecases)
    - [1.2 Best Practices](#12-best-practices)
        - [1.2.1 At Home](#121-at-home)


## 1.0 TODO
- need uses for docker
- why docker??? 

## 1.1 Use cases
-

## 1.2 Best Practices
- use it for data science courses
### 1.2.1 At Home
- use for python projects 

## 1.3 Notes 

## 1.4.1 Installing Docker on Centos7 (long Method)

`less /etc/os-release`  check OS version

`sudo yum install -y yum utils device-mapper-persistent-data lvm2`

`sudo yum install -y yum-utils`   -install yum utils to be able to access  `yum config manager`

`sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.rep`   -add repo for installing docker

`sudo yum install docker-ce`  - install docker ce (community edition)

`sudo systemctl enable docker` -enable docker

`sudo systemctl start docker` - start docker

`sudo docker run hello-world` -test the docker client  connection to docker daemon and was able tp pull docker image from dockerhub. You need sudo because the default  user on the ec2(ceontos in this case) does not come with docker running privileges'

`sudo usermod -a -G docker centos`  grant user called 'centos' permission to run docker. NB REMEBER to exit then re-enter the terminal to ensure the permissions get changed

## 1.4.2 Installing Docker on Centos7 (Short method)

`wget -q0- https://get.docker.com |sh`



## 1.5 Docker Commands



`docker ps -a`  - view containers and see which ones are running and for how long etc and other important stats

`docker run -d --name webserver nginx:latest`   - the -d means run in the background, creates a nginx webserver in a docker container

`docker images`  - shows all docker images on the local machine

## 1.6 Docker Ports

- Dockers containers can use the same port BUT must use different host ports. The host port decides which container the communication will go to. Container port is only used for internal container usage

- Host ports need to be different
- Examples below:-
- Nginx container
  - Host port :80
  - Container port:80
- Tomcat container
  - Host port:8081
  - Container port:8080
- Nginxcointainer2
  - Host port:81
  - Container port:80   --notice this is the same port as the first container(Nginx) BUT this port is on a different container and not the first container
