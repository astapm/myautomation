#! /usr/bin/env python

# Скрипт для автоматизации записи значений давления и пульса в файл csv
# Ввод данных через аргументы командной строки
# Порядок аргументов следующий:
#
#     $ python tone2csv-cli.py <д> <с> <п> <д> <в> <н>
#
# д - диастолическое давление
# с - систолическое давление
# п - пульс
# д - дата
# в - время
# н - примечание
# Значения проверяются на корректность
# В случае некорректных данных делается запись в файл ошибок mytone_err.csv
# Дата, время, и примечание могут быть пустыми -- ""
# Автоматически по умолчанию записывает текущую дату и время

from datetime import datetime
import csv
import sys
import argparse
# Модуль mylib.py.
# Функции проверки вводимых числовых значений, даты, времени, длины строки
#    valid_date(date_str, format_date): Проверяет date_str на соответствие формату даты format_date (напр.,"%Y-%m-%d")
#    valid_time(time_str, format_time): Проверяет time_str на соответствие формату времени format_time (напр., "%H:%M")
#    valid_lenstr(note_str, max_len):  Проверяет строку note_str на длину max_len
#    valid_digit(digit, min_digit, max_digit): Проверяет число на соответствие диапазону min_digit - max_digit
from mylib import valid_date, valid_time, valid_lenstr, valid_digit

# Файл для записи данных лавления и пльса
# Если файла нет, то он будет создан в текущем каталоге
FILENAME = "mytone.csv"

# Файл для записи в лог ошибок данных лавления и пльса
# Если файла нет, то он будет создан в текущем каталоге
FILENAME_ERR = "mytone_err.csv"

# Флаг ввода некорректного параметра
error_flag = False

def createParser ():
    '''Функция для определения списка параметров командной строки'''

    parser = argparse.ArgumentParser()
    parser.add_argument('diast')
    parser.add_argument('systol')
    parser.add_argument('pulse')
    parser.add_argument('date')
    parser.add_argument('time')
    parser.add_argument('note')
 
    return parser

parser = createParser()
namespace = parser.parse_args()

# Проверяем аргумент верхнего давления
if namespace.diast.isdigit():
    namespace.diast = int(namespace.diast)
    if valid_digit(namespace.diast,80,300) == False:
        error_flag = True
        namespace.diast = "Err: " + str(namespace.diast)
else:
    error_flag = True
    namespace.diast = namespace.diast + "!!!"

# Проверяем аргумент нижнего давления
if namespace.systol.isdigit():
    namespace.systol = int(namespace.systol)
    if valid_digit(namespace.systol,40,200) == False:
        error_flag = True
        namespace.systol = "Err: " + str(namespace.systol)
else:
    error_flag = True
    namespace.systol = "Err: " + str(namespace.systol)

# Проверяем аргумент пульса
if namespace.pulse.isdigit():
    namespace.pulse = int(namespace.pulse)
    if valid_digit(namespace.pulse,30,200) == False:
        error_flag = True
        namespace.pulse = "Err: " + str(namespace.pulse)
else:
    error_flag = True
    namespace.pulse = "Err: " + str(namespace.pulse)

# Проверяем аргумент время
if namespace.time == "":
    namespace.time = datetime.today().strftime("%H:%M")
if valid_time(namespace.time, "%H:%M") == False:
    error_flag = True
    namespace.time = "Err: " + namespace.time

# Проверяем аргумент дату
if namespace.date == "":
    namespace.date = datetime.today().strftime("%Y-%m-%d")
if valid_date(namespace.date, '%Y-%m-%d') == False:
    error_flag = True
    namespace.date = "Err: " + namespace.date

# Проверяем аргумент примечание
if valid_lenstr(namespace.note, 150) == False:
    error_flag = True
    namespace.note = "Err: " + namespace.note

# Записываем в файл
if error_flag == False:
    with open(FILENAME, "a", newline="") as file:
        tone = [namespace.date,namespace.time,namespace.diast,
               namespace.systol,namespace.pulse,namespace.note]
        writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(tone)
else:
    with open(FILENAME_ERR, "a", newline="") as file:
        tone = [namespace.date,namespace.time,namespace.diast,
               namespace.systol,namespace.pulse,namespace.note]
        writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(tone)
