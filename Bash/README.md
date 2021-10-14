## Operating system details  
`cat /etc/os-release` 

## switch user

`su user`

## update system

`sudo dnf update`

## present working directory  
`pwd`  

## current user  
`whoami`  

## install locate command
`sudo dnf install mlocate`  

 - NB: make sure to use the code below immediately!! after the install command above. This is to update the locations in your computer to be able to search/locate files and folders 
 - The code below is only run once a day, so run it first each time you want to locate a file 

 `sudo updatedb`

## combined install and locate command for janevieve

    sudo dnf install mlocate
    sudo updatedb
    locate bin/postgres
    /usr/pgsql-13/bin/postgres -V

## functions and error checking
below is a single line function  

`ls this_file_does_not_exist.txt || { echo "The update command has failed"; exit 1; }`

-NB this command switches you back and forth between the users "ec2-user" and "root" each time it "exits 1"