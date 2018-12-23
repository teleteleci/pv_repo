#!/bin/bash

echo "" > rslt.txt
a = $1
for ((i=1; i<=$1; i++))
do
    echo $i
    $(python app.py >> rslt.txt) &
done
