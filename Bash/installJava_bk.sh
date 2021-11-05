#!/bin/bash

CURRDIR=$(pwd)
JAVA_DL=""
JAVA_TMP=""
HOME_DIR=($HOME)
JAVA_VERS=""
USER_INSTALL_DIR=""

trap 'rm -f $CURRDIR/$JAVA_TMP' EXIT HUP INT TERM

RH_RELEASE=$(cat /etc/*release | cut -d = -f2 | sed 's/"//g' | cut -d "." -f1 | sed -n '2 p')
if [ "$RH_RELEASE" == 8 ]; then
echo "RHEL 8 detected, continuing..."
else
echo "The RHEL version is not supported" && exit 1
fi

pre_req() {
#Check existence of Java on the node
if [ -d $USER_INSTALL_DIR/bin ]; then
echo "IBM Java is already installed on the host" >&2 && exit 1
else
echo "IBM Java is not present on the node, continuing..."
fi
sudo yum update -y &>/dev/null
if [ $? -eq 0 ]; then
echo "YUM update success"
else
echo "YUM update failed >&2" && exit 1
fi
RPM_CHECK=$(sudo rpm -qa wget | wc -l)
if [ "$RPM_CHECK" -eq 1 ]; then
echo "WGET already installed"
else 
sudo yum install wget -y &>/dev/null
if [ $? -ne 0 ]; then
echo "Installation of WGET failed" >&2 && exit 1
else 
echo "Installation of WGET completed"
fi
fi
}

install() {
# Set vars,download & install the package
echo "Downloading the package, please wait..."
sudo wget $JAVA_DL &>/dev/null
if [ $? -eq 0 ]; then
echo "Java downloaded successfully"
else
echo "Java download failed" >&2 && exit 1
fi
export _JAVA_OPTIONS="-Dlax.debug.level=3 -Dlax.debug.all=true"
export LAX_DEBUG=1
tee installer.properties <<EOF
INSTALLER_UI=silent
LICENSE_ACCEPTED=TRUE
USER_INSTALL_DIR=$USER_INSTALL_DIR
EOF
chmod +x $CURRDIR/$JAVA_TMP && $CURRDIR/$JAVA_TMP -i silent -f installer.properties
echo " my IBM install  version error code is " $?
read -p "Press enter to continue"
if [ $? -ne 0 ]; then
echo "installation of IBM Java failed" >&2 && exit 1
else 
echo "installation of IBM Java completed"
fi
}
echo " my IBM install version error code is " $?
read -p "Press enter to continue"
post_install(){
echo "this is my user install directory:" $USER_INSTALL_DIR
echo "this is my home directory: " $HOME_DIR
read -p "Press enter to continue"

echo "export PATH=$USER_INSTALL_DIR/bin:$PATH" >> $HOME_DIR/.bash_profile && source $HOME_DIR/.bash_profile
java -version 
echo " my version error code is " $?
read -p "Press enter to continue"

if [ $? -eq 0 ]; then
echo "Java post-check and config completed"
else
echo "Java post-check and config failed" >&2 && exit 1
fi
}

echo -n 'Please choose the Java version to be installed (supported versions: 70,71,8,11): '
while :
do
  read JAVA_VERS
  case $JAVA_VERS in

	70)
		JAVA_DL=$(echo "http://public.dhe.ibm.com/ibmdl/export/pub/systems/cloud/runtimes/java/7.0.10.90/linux/x86_64/ibm-java-x86_64-sdk-7.0-10.90.bin")
		JAVA_TMP=(ibm-java-x86_64-sdk-7.0-10.90.bin)
		USER_INSTALL_DIR=/opt/ibm/java-x86_64-70
		pre_req; install; post_install
		break
		;;
	71)
		JAVA_DL=$(echo "http://public.dhe.ibm.com/ibmdl/export/pub/systems/cloud/runtimes/java/7.1.4.90/linux/x86_64/ibm-java-x86_64-sdk-7.1-4.90.bin")
		JAVA_TMP=(ibm-java-x86_64-sdk-7.1-4.90.bin)
		USER_INSTALL_DIR=/opt/ibm/java-x86_64-71
		pre_req; install; post_install
		break
		;;
	8)
		JAVA_DL=$(echo "http://public.dhe.ibm.com/ibmdl/export/pub/systems/cloud/runtimes/java/8.0.6.36/linux/x86_64/ibm-java-x86_64-sdk-8.0-6.36.bin")
		JAVA_TMP=(ibm-java-x86_64-sdk-8.0-6.36.bin)
		USER_INSTALL_DIR=/opt/ibm/java-x86_64-80
		pre_req; install; post_install
		break
		;;

	11)	JAVA_DL=$(echo "https://public.dhe.ibm.com/ibmdl/export/pub/systems/cloud/runtimes/java/11.0.12.0/linux/x86_64/ibm-semeru-certified-jdk_x64_linux_11.0.12.0.bin")
		JAVA_TMP=(ibm-semeru-certified-jdk_x64_linux_11.0.12.0.bin)
		USER_INSTALL_DIR=/opt/ibm/java-x86_64-11
		pre_req; install; post_install
		break
		;;

	*)	echo "Invalid selection, exiting" && exit 1
		break
		;;

  esac
done
echo 
