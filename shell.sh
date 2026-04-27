#!/bin/bash
echo "Enter directory path:"
read dir

if [ -d "$dir" ]
then
    ls "$dir"
else
    echo "Directory does not exist"
fi
