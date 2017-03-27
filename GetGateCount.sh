#!/bin/bash

DIR="esop_files_w"
TXT_LIST="esop_file_list.txt"

## This is important for the shared cubed synethsis program to work
mkdir $DIR
touch $TXT_LIST

## Move the esop file to esop_files_w folder
## and write each file to esop_file_list.txt
mv $1 $DIR

for file in "$DIR"/*
do
  echo "Filename: $file"
  echo $file | cut -d'/' -f 2 &> $TXT_LIST
done


## Execute Improved_Shared_Cube_Synthesis program
echo "Gathering gate count from .esop files..."

java -jar ./Improved_Shared_Cube_Synthesis.jar &> metrics.txt

echo "Finished shared cube synthesis"

## Clean up
rm -rf $DIR
rm $TXT_LIST
