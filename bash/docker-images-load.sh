#!/bin/bash

# Load the image from the specified directory or the directory where this script is located to docker.
# example:
# bash docker-images-load.sh
# bash docker-images-load.sh images

for filename in $(ls $1)
do
    if [ ${filename##*.} = tar ];then
        docker load < $filename
    fi
done
