#!/bin/sh
# This scrip is for pushing my code to gitlab
echo Starting Push for $UID, Please enter Commit Message:
read varMessage
git add .
git commit -m "$varMessage"
git push "https://gitlab-ci-token:TqCszEqvPgUyWoA-UZtC@gitlab.com/rwaki/rwakipythonpractice.git" master