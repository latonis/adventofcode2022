#!/bin/bash

if [[ $1 =~ [0-9]{1,2} ]]; then
    mkdir -p $1
    cp ./template/* $1/
    echo "Directory for day $1 created!"
else 
    echo "Directory not created, invalid input!"
fi
