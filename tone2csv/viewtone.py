#! /usr/bin/env python

# Скрипт для для просмотра значений давления и пульса из файла csv
# По умолчанию выводятся десять последних записей

# TODO Удаление последней записи
# TODO Показать среднее значения параметров за месяц
# TODO Информация о времени начала записей
# TODO Создание графика за период
# TODO Выбор периода
# TODO Редактироваеие записи 
# TODO Форматирование вывода

import csv

name_fiile = "mytone.csv"
csv_delimeter =";"
num_line_out = 10

with open(name_fiile) as f:
    num_line = (sum(1 for _ in f))

if num_line < num_line_out:
    with open(name_fiile, newline='') as File:  
        reader = csv.reader(File, delimiter=csv_delimeter)
        for row in reader:
            print(row[0],row[1],row[2],row[3],row[4],row[5])
else:
    count = 0
    with open(name_fiile, newline='') as File:  
        reader = csv.reader(File, delimiter=csv_delimeter)
        for row in reader:
            if count >= num_line - num_line_out:
                print(row[0],row[1],row[2],row[3],row[4],row[5])
            count += 1

print("Programm terminated normally")
