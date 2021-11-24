
<img src="images/bashDarkLogo.png" alt="drawing" width="400" height="174"/>  

# Welcome to BASH!!  

- Bash supports regular expressions or regex!
- Using tab , autocomplete file names
- touch can be used to create several files at a time, as long as you separate them by space e.g 
`touch file1.txt file3.txt file3.txt`



## enter a directory e.g the famous opt directory

`cd /opt`  

or
`cd /opt/folderIwant` 

or  to go straight to the `home` directory  

`cd ~`

or  to go straight to the `root` directory 

`cd /`  

## Identify the shell of your system

`echo $0`

## Operating system details  
`cat /etc/os-release` 

## See contents 
`cat filename.txt`

## less
- less is a much better version of cat, does the same thing except opens the contents of your search in a new window
- All you need to do is remember to use `q` to exit the window and return to your previous terminal screen  

- `less filename.txt`  
- `less /etc/os-release` 

- To display numbers on the search use the `N` flag/option  NOTE: the N must be capitalized  e.g  
`less -N  /etc/os-release` 

## Assigning variables
- please please please!!! note: bash HATES spaces in assignments, e.g:-
- `java_ver = $1`   -DON'T do This
- `java_ver=$1`      - DO This!!
- If you make the mistake above, you will get `command not found`
## My current instances of interest
`ssh -i "rwakiPython_v2.pem" ec2-user@ec2-52-201-31-127.compute-1.amazonaws.com`   --for SUSE Linux
`ssh -i "rwakiPython_v2.pem" ec2-user@ec2-54-174-4-0.compute-1.amazonaws.com `     --for RHEL

## add user


## add password for new user

`passwd`


## (su)switch user

`su user`
`sudo su`   - change to root user in ec2


## go up a directory, or to back out of directory(remember the space between the CD and the dots)

`cd .. ` 
## move directly to you root directory

`cd /`
## update system (RHEL 8 and above)

`sudo dnf update`

## move a file using verbose command (recommended)
- using the verbose command, just summarizes for you what happened during the copy command e.g   

`cp -v file2beCopied.txt /home/newDirectory`  

output:-

`file2beCopied.txt -> /home/newDirectory`
## present working directory  
`pwd`  

## current user  
`whoami`  

## install program from wget(RHEL 8 and later)

`sudo dnf install wget`
## make file executable in linux

        > chmod +x hello
        > ./hello
        hi


## install locate command
`sudo dnf install mlocate`  

 - NB: make sure to use the code below immediately!! after the install command above. This is to update the locations in your computer to be able to search/locate files and folders 
 - The code below is only run once a day, so run it first each time you want to locate a file 

 `sudo updatedb`

## combined install and locate command 

    sudo dnf install mlocate -y
    sudo updatedb
    locate bin/postgres
    /usr/pgsql-13/bin/postgres -V

## functions and error checking
below is a single line function  

`ls this_file_does_not_exist.txt || { echo "The update command has failed"; exit 1; }`

-NB this command switches you back and forth between the users "ec2-user" and "root" each time it "exits 1"

## change file to executable

`sudo chmod +x filename.bin`
chmod +x ibm-java-ppc64-sdk-8.0-6.36.bin


## Recording macros

https://stackoverflow.com/questions/1527784/what-is-vim-recording-and-how-can-it-be-disabled 

## Add stuff to Path

export PATH=/opt/rh/devtoolset-6/root/usr/bin${PATH:+:${PATH}}

e.g
export PATH="/opt/ibm/java-x86_64-80/bin:$PATH"

### testing path to linux program
`java -version`

## updating source




## access .bashrc
 `vi .bashrc`
## Add stuff to bash profile

export PATH=/opt/ibm/java-x86_64-80/bin:$PATH>>~/.bash_profile  
export PATH=/opt/ibm/java-x86_64-80/bin:$PATH >> ~/.bashrc 
source $HOME/.bashrc


- add this to .bashrc
echo "export PATH="/opt/ibm/java-x86_64-80/bin:$PATH"" >> semaText.txt

## Delete contents of a file 
`truncate -s 0 filename.txt`

echo -n "export PATH="/opt/ibm/java-x86_64-80/bin:$PATH"" >> semaText.txt

echo "export PATH="/opt/ibm/java-x86_64-80/bin:$PATH" ">> semaText.txt
echo export PATH=\"/opt/ibm/java-x86_64-80/bin:$PATH\">> semaText.txt

## show human readable path
`echo "${PATH//:/$'\n'}"`


## Best utilities to install in new linux instance for productivity
- App for zip and unzip install files
- `yum install zip unzip -y`
- Neofetch
- `sudo yum install neofetch`

        neofetch --ascii_distro ubuntu
        neofetch --ascii_distro archlinux
        neofetch --ascii_distro fedora
        neofetch --ascii_distro manjaro
        neofetch --ascii_distro debian
        neofetch --ascii_distro rhel

PATH=$PATH:/opt/ibm/java-x86_64-80/bin

C:\Users\Burudani\Documents\mainPythonFolder_v1\Bash\exprimebash.sh firstpipe "22"


chmod +x testBashScript.sh


echo export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64 >> ${HOME}/.bashrc  
echo export PATH="/opt/ibm/java-x86_64-80/bin:$PATH" >> ~/.bashrc && source ~/.bashrc

## 11/15/2021
- He used  chmod 755 for the script
- ./installJava.sh post_install 11 && source ~/.bashrc

cat /root/.bashrc

./installJava.sh pre_req 8
./installJava.sh install 8
./installJava.sh post_install 8 && source ~/.bashrc


sh installJava.sh install 11
sh installJava.sh post_install 11
