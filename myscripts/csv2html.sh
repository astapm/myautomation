#!/bin/bash

# Скрипт переводит csv-файл в html-таблицу

nameFileCSV="mytone.csv"
# nameFileHTML="mytone.html"
CSVseparator=";"

echo "<html>"
echo "<head>"
echo "  <title>"
echo "    Перевод csv-файла $nameFileCSV в таблицу html"
echo "  </title>"
echo "</head>"
echo "<body>"

echo "<table>"
IFS=$'\n'
for var in $(cat $nameFileCSV)
  do
  echo "<tr>"
  IFS=$CSVseparator
    for dt in ${var[*]}
    do
    echo "<td>"
    echo $dt
    echo "</td>"
    done
  echo "</tr>"
  done
echo "</table>"

echo "</body>"
echo "</html>"
