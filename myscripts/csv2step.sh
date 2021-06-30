#!/bin/bash

# Скрипт выврдит csv-файл nameFileCSV в таблицу-лесенку

nameFileCSV="mycsv.csv"
prefix=" "
CSVseparator=";"

IFS=$'\n'
for row in $(cat $nameFileCSV)
do
count=0
IFS=$CSVseparator
  for var in ${row[*]}
  do
    for((i=0;i<$count;i++))
    do                         
    echo -n $prefix
    done
  count=$(($count + 1))
  echo $var
  done
done
