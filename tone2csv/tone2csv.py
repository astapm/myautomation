#! /usr/bin/env python

# Скрипт для автоматизации записи значений давления и пульса в файл csv
# Ввод данных последовательно в диалоговом режиме
# Значения проверяются на корректность
# Автоматически по умолчанию записывает текущую дату и время

from datetime import datetime
import csv
# Модуль mylib.py.
# Функции проверки вводимых числовых значений, даты, времени, длины строки
#    valid_date(date_str, format_date): Проверяет date_str на соответствие формату даты format_date (напр.,"%Y-%m-%d")
#    valid_time(time_str, format_time): Проверяет time_str на соответствие формату времени format_time (напр., "%H:%M")
#    valid_lenstr(note_str, max_len):  Проверяет строку note_str на длину max_len
#    valid_digit(digit, min_digit, max_digit): Проверяет число на соответствие диапазону min_digit - max_digit
# Функции для ввода данных и проверки на корректность типа данных
# dialog -- строка-приглашение для ввода данных
# dialog_error -- строка-вывод о некорректном вводе даннах
#    input_valid_digit(min_digit, max_digit, dialog, dialog_error): Функция для ввода числа и его проверки на минимум и максимум
#    input_valid_date(format_date, dialog, dialog_error): Функция для ввода даты в формате "%Y-%m-%d" и её проверки
#    input_valid_time(format_time, dialog, dialog_error): Функция для ввода времени в формате "%H:%M" и его проверки
#    input_valid_string(limit, dialog, dialog_error): Функция для ввода текстовой строки длинной не более limit
from mylib import *

# Имя файл для записи данных давления и пульса
# Если файла нет, то он будет создан в текущем каталоге
FILENAME = "mytone.csv"

csv_delimiter = ";"

# main
print("Запись значений давления и пульса в файл {}\n".format(FILENAME))

# Последовательное приглашение ввести данные
y = True
while y == True:
    print("Введите данные:")
    diastolic = input_valid_digit(80, 300,
                                  "Диастолическое верхнее давление (80-300): ",
                                  "ОШИБКА! {} -- некорректное значение для верхнего давления")
                                  
    systolic  = input_valid_digit(40, 200,
                                  "Систолическое нижнее давление (40-200): ",
                                  "ОШИБКА! {} -- некорректное значение для нижнего давления")
                                 
    pulse   =   input_valid_digit(30, 200,
                                  "Пульс (30-200): ",
                                  "ОШИБКА! {} -- некорректное значение для пульса")
                                  
    date    =    input_valid_date('%Y-%m-%d',
                                  "Дата -- ГГГГ-ММ-ДД (по умолчанию текущая дата): ",
                                  "ОШИБКА! {} -- некорректное значение для даты")
                                  
    hour    =    input_valid_time("%H:%M",
                                  "Время -- ЧЧ:ММ (по умолчанию текущее время): ",
                                  "ОШИБКА! {} -- некорректное значение для времени")
                                  
    note   =   input_valid_string(150,
                                  "Примечание к записи. Лимит символов --  {}: ",
                                  "ОШИБКА! Превышен лимит {} символов")
                                  
                                  
                                  
    print("---")
    print("Это правильные значения?")
    print("Верхнее давление: ", diastolic)
    print("Нижнее давление: ", systolic)
    print("Пульс: ", pulse)
    print("Примечание: ", note)
    print("Дата, время: ", date, hour)
    choice = input("[<Ввод> -Да, <н> - Нет] ;")
    if choice != "н":
        y = False

with open(FILENAME, "a", newline="") as file:
    tone = [date,hour,diastolic,systolic,pulse,note]
    writer = csv.writer(file, delimiter=csv_delimiter)
    writer.writerow(tone)

print("---")
print("Записано в файл: ",str(date)+";"+str(hour)+";"+str(diastolic)+";"+str(systolic)+";"+str(pulse)+";"+note+";")

print("Programm terminated normally")
