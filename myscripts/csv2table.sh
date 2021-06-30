#!/bin/bash

# Скрипт переводит csv-файл в форматированную таблицу

# МОДИФИЦИРОВАТЬ ЭТИ ПЕРЕМЕННЫЕ
# Файл CSV
nameFileCSV="mytone2.csv"
# Строка спецификаторов для вывода таблицы
table_format=("%11s" "%6s" "%4d" "%3d" "%3d" " %s")
# Разделитель полей CSV
CSVseparator=";"

IFS=$'\n'
for row in $(cat $nameFileCSV)
do
  IFS=$";"
  count=0
  printf "|"
  for var in ${row[*]}
    do
    printf "${table_format[$count]} |" $var
    count=$(($count + 1))
  done
printf "\n"
done
