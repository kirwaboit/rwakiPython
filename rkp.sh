#!/bin/sh
# This scrip is for pushing my code to gitlab
git add .
git commit -m "using a script to send my code to gitlab"
git push "https://gitlab-ci-token:TqCszEqvPgUyWoA-UZtC@gitlab.com/rwaki/rwakipythonpractice.git" master
