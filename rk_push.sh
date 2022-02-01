#!/bin/sh
# This script is for pushing my code to gitlab
echo Starting Push for user :  $(whoami), Please enter Commit Message below:
read varMessage  # this prompts the user for an input messsage , then saves the result in a variable
git add .
#git commit -m "$(whoami): $varMessage"
git commit -m  "$varMessage"
git push "https://gitlab-ci-token:gjsNyxgD4aMhnjL_iAM_@gitlab.com/rwaki/rwakipythonpractice.git" master



