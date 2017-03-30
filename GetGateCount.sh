#!/bin/bash

DIR="esop_files_w"
TXT_LIST="esop_file_list.txt"

## This is important for the shared cubed synethsis program to work
mkdir $DIR
touch $TXT_LIST

file=$1
metricsFilename=${file%.*}

## Move the esop file to esop_files_w folder
## and write each file to esop_file_list.txt
mv $1 $DIR

for file in "$DIR"/*
do
  echo $file | cut -d'/' -f 2 &> $TXT_LIST
done


## Execute Improved_Shared_Cube_Synthesis program
echo "Gathering gate count from $metricsFilename.esop file..."

java -jar ./Improved_Shared_Cube_Synthesis.jar &>  "$metricsFilename.txt"

## Clean up
rm -rf $DIR
rm $TXT_LIST
