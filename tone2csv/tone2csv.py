#! /usr/bin/env python

# Скрипт для автоматизации записи значений давления и пульса в файл csv
# Ввод данных последовательно в диалоговом режиме
# Значения проверяются на корректность
# Автоматически по умолчанию записывает текущую дату и время

# ERROR Line 40
# ERROR Line 54

# TODO сделать ввод через аргументы скрипта
# TODO реализовать тексты диалогов чеоез list
# TODO реализовать диалог проверки наличия и создания нового файла
# TODO сделать диалог выхода из скрипта


import datetime
import csv

# Файл для записи данных лавления и пльса
# Если файла нет, то он будет создан в текущем каталоге
FILENAME = "mytonecsv.csv"

# Cообщения для диалогового интерфейса
dialog1 = "Введиите диастолическое верхнее давление от 80 до 300: "
dialog_error1 = " -- это некорректное значение для верхнего давления"
dialog2 = "Введиите систолическое нижнее давление от 40 до 200: "
dialog_error2 = " -- некорректное значение для нижнего давления"
dialog3 = "Введиите пудьс от 30 до 200: "
dialog_error3 = " -- это некорректное значение для пульса"
dialog4 = "Введиите дату -- ГГГГ-ММ-ДД (по умолчанию текущая дата): "
dialog_error4 = " -- это некорректное значение для даты"
dialog5 = "Введиите время -- ЧЧ:ММ (по умолчанию текущее время): "
dialog_error5 = " -- это некорректное значение для времени"
dialog6 = "Введиите примечание. Лимит символов - "
dialog_error6 = " -- Строка превысила лимит"

# Функции проверки вводимых числовых значений, даты, времени, длины строки
def valid_date(date_str, format_date):
    '''Проверяет date_str на соответствие формату даты format_date (напр.,"%Y-%m-%d")'''

    try:
        # ERROR AttributeError: module 'datetime' has no attribute 'strptime'
        if date_str != datetime.strptime(date_str,format_date).strftime(format_date):
            raise ValueError
        return True
    except ValueError:
        return False

def valid_time(time_str, format_time):
    '''Проверяет time_str на соответствие формату времени format_time (напр., "%H:%M")'''

    try:
        # ERROR AttributeError: module 'datetime' has no attribute 'strptime'
        if time_str != datetime.strptime(time_str,format_time).strftime(format_time):
            raise ValueError
        return True
    except ValueError:
        return False

def valid_lenstr(note_str, max_len):
    '''Проверяет строку note_str на длину max_len'''

    try:
        if len(note_str) > max_len:
            raise ValueError
        return True
    except ValueError:
        return False

def valid_digit(digit, min_digit, max_digit):
    '''Проверяет число на соответствие диапазону min_digit - max_digit'''

    try:
        if digit < min_digit or digit > max_digit:
            raise ValueError
        return True
    except ValueError:
        return False
    
# Функция для ввода числовых данных и их проверки на минимум и максимум
# В случае некорректного значения повторяет ввод
def input_valid_digit(min_digit, max_digit, dialog, dialog_error):
    '''Функция для ввода числа и его проверки на минимум и максимум'''

    f = True
    while f == True:
        digit = input(dialog)
        if digit.isdigit():
            digit = int(digit)
            if valid_digit(digit, min_digit, max_digit) != True:
                print("ОШИБКА!",digit,dialog_error)
            else:
                f = False
        else:
            print("ОШИБКА!",digit,dialog_error)
    return digit

# Функция для ввода даты и её проверки на корректность
# В случае некорректного значения повторяет ввод
def input_valid_date(format_date, dialog, dialog_error):
    '''Функция для ввода даты и её проверки'''

    x = True
    while x == True:
        date = input(dialog)
        if date == "":
            dt = datetime.datetime.now()
            date = dt.strftime(format_date)
            x = False
        else:
            if valid_date(date, format_date) == True:
                x = False
            else:
                print("ОШИБКА!", date, dialog_error)
    return date

# Функция для ввода времени и проверки на корректность
# В случае некорректного значения повторяет ввод
def input_valid_time(format_time, dialog, dialog_error):
    '''Функция для ввода времени и его проверки'''

    x = True
    while x == True:
        time = input(dialog)
        if time == "":
            dt = datetime.datetime.now()
            time = dt.strftime(format_time)
            x = False
        else:
            if valid_time(time, format_time) == True:
                x = False
            else:
                print("ОШИБКА!", time, dialog_error)
    return time

# Функция для ввода текстовой строки и проверки лимита длинны
# В случае превышения лимита повторяет ввод
def input_valid_string(limit, dialog, dialog_error):
    '''Функция для ввода текстовой строки длинной не более limit'''

    x = True
    while x == True:
        note = input(dialog + str(limit) + " символов: ")
        if valid_lenstr(note, limit) == True:
           x = False
        else:
            print("ОШИБКА!", dialog_error, limit, "символов")
    return note

# main
print("Запись значений давления и пульса в файл mytonecsv.csv\n")

y = True
while y == True:
    diastolic = input_valid_digit(80,300,dialog1,dialog_error1)
    systolic = input_valid_digit(40,200,dialog2,dialog_error2)
    pulse = input_valid_digit(30,200,dialog3,dialog_error3)
    date = input_valid_date('%Y-%m-%d', dialog4, dialog_error4)
    hour = input_valid_time("%H:%M",dialog5, dialog_error5)
    note = input_valid_string(150, dialog6, dialog_error6)
    print("---")
    print("Это правильные значения?")
    print("Верхнее давление: ", diastolic)
    print("Нижнее давление: ", systolic)
    print("Пульс: ", pulse)
    print("Примечание: ", note)
    print("Дата, время: ", date, hour)
    choice = input("[<Ввод> -Да, <н> - Нет]")
    if choice != "н":
        y = False

with open(FILENAME, "a", newline="") as file:
    tone = [date,hour,diastolic,systolic,pulse,note]
    writer = csv.writer(file)
    writer.writerow(tone)

print("---")
print("Записано в файл: ",str(date)+";"+str(hour)+";"+str(diastolic)+";"+str(systolic)+";"+str(pulse)+";"+note+";")
print("Programm terminated normally")
