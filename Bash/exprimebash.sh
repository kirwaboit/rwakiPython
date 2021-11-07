#!/bin/sh
CURRDIR=$(pwd)
JAVA_DL=""
JAVA_TMP=""
HOME_DIR=($HOME)
JAVA_VERS= "$2"
#USER_INSTALL_DIR=""


echo "hello world"
echo "$2"
#echo "JAVA_VERS"
read -p "Press enter to continue"

firstpipe() {
echo "Parameter #1 is $1"
echo "Parameter #2 is $2"
echo "Variable JAVA_VERS  is $JAVA_VERS"
read -p "Press enter to continue"

}

#firstpipe "${2}"
firstpipe "${1}"
firstpipe "${2}"