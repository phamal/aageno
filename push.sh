#!/bin/sh
echo "Pushing latest local changes"
cd /apps/code/aageno/
git add *
git commit -m"$1"
git push


