#! /usr/bin/env python

# Скрипт для автоматизации записи значений давления и пульса в файл csv
# Ввод данных последовательно в диалоговом режиме
# Значения проверяются на корректность
# Автоматически по умолчанию записывает текущую дату и время

from datetime import datetime, date
import time
import csv

# Файл для записи данных лавления и пльса
# Если файла нет, то он будет создан в текущем каталоге
FILENAME = "mytone.csv"

# Cообщения для диалогового интерфейса.
dialog1 = ["Впкдите диастолическое верхнее давление (80-300): "]
dialog_error1 = ["ОШИБКА!", "-- это некорректное значение для верхнего давления"]
dialog2 = ["Введите систолическое нижнее давление (40-200): "]
dialog_error2 = ["ОШИБКА!", "-- некорректное значение для нижнего давления"]
dialog3 = ["Введите пульс (30-200): "]
dialog_error3 = ["ОШИБКА!", "-- это некорректное значение для пульса"]
dialog4 = ["Введите дату -- ГГГГ-ММ-ДД (по умолчанию текущая дата): "]
dialog_error4 = ["ОШИБКА!", "-- некорректное значение для даты"]
dialog5 = ["Введите время -- ЧЧ:ММ (по умолчанию текущее время): "]
dialog_error5 = ["ОШИБКА!", "-- это некорректное значение для времени"]
dialog6 = ["Введите примечание. Лимит символов - ", ": "]
dialog_error6 = ["ОШИБКА!", "Строка превысила лимит", "символов"]

# Функции проверки вводимых числовых значений, даты, времени, длины строки
def valid_date(date_str, format_date):
    '''Проверяет date_str на соответствие формату даты format_date (напр.,"%Y-%m-%d")'''

    try:
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
        digit = input(dialog[0])
        if digit.isdigit():
            digit = int(digit)
            if valid_digit(digit, min_digit, max_digit) != True:
                print(dialog_error[0],digit,dialog_error[1])
            else:
                f = False
        else:
            print(dialog_error[0],digit,dialog_error[1])
    return digit

# Функция для ввода даты и её проверки на корректность
# В случае некорректного значения повторяет ввод
def input_valid_date(format_date, dialog, dialog_error):
    '''Функция для ввода даты и её проверки'''

    x = True
    while x == True:
        date_str = input(dialog[0])
        if date_str == "":
            date_str = datetime.today().strftime("%Y-%m-%d") 
            x = False
        else:            
            if valid_date(date_str, format_date) == True:
                x = False
            else:
                print(dialog_error[0], date_str, dialog_error[1])
    return date_str

# Функция для ввода времени и проверки на корректность
# В случае некорректного значения повторяет ввод
def input_valid_time(format_time, dialog, dialog_error):
    '''Функция для ввода времени и его проверки'''

    x = True
    while x == True:
        time_str = input(dialog[0])
        if time_str == "":
            time_str = time.strftime("%H:%M", time.localtime())
            x = False
        else:
            if valid_time(time_str, format_time) == True:
                x = False
            else:
                print(dialog_error[0], time_str, dialog_error[1])
    return time_str

# Функция для ввода текстовой строки и проверки лимита длинны
# В случае превышения лимита повторяет ввод
def input_valid_string(limit, dialog, dialog_error):
    '''Функция для ввода текстовой строки длинной не более limit'''

    x = True
    while x == True:
        note = input(dialog[0] + str(limit) + dialog[1])
        if valid_lenstr(note, limit) == True:
           x = False
        else:
            print(dialog_error[0], dialog_error[1], limit, dialog_error[2])
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

