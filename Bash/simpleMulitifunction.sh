#!/bin/bash
# for calling two functions back to back
ls1(){
        echo "Hello World"
}

ls2(){
        echo "Testing"
}

#to call these back to back, just enter "source simpleMultifunction.sh;ls1;ls2"