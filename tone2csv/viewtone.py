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
import os

with open('mytone.csv') as f:
    num_line = (sum(1 for _ in f))

if num_line < 10:
    with open('mytone.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row[0],row[1],row[2],row[3],row[4],row[5])
else:
    r = os.system("tail -n 10 mytone.csv")
    print(r)

print("Programm terminated normally")
 
