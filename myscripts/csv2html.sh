#!/bin/bash

# Скрипт переводит csv-файл `nameFileCSV` в html-таблицу

nameFileCSV="mycsv.csv"
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
    for td in ${var[*]}
    do
    echo "<td>"
    echo $td
    echo "</td>"
    done
  echo "</tr>"
  done
echo "</table>"

echo "</body>"
echo "</html>"
