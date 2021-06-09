""" Функции необходимые для проверки типов двнных -- даты, времени, длины строки, диапазона чисел"""

# Функции проверки правильности вводимых значений даты, времени, длины строки, диапазона чисел.

from datetime import datetime

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
        

# Функции для ввода данных и проверки на корректность типа данных
# dialog -- строка-приглашение для ввода данных
# dialog_error -- строка-вывод о некорректном вводе даннах
 
# Функция для ввода числовых данных и их проверки на минимум и максимум
# В случае некорректного значения повторяет ввод
def input_valid_digit(min_digit, max_digit, dialog, dialog_error):
    '''Функция для ввода числа и его проверки на минимум и максимум'''

    x = True
    while x == True:
        digit = input(dialog)
        if digit.isdigit():
            digit = int(digit)
            if valid_digit(digit, min_digit, max_digit) != True:
                print(dialog_error.format(digit))
            else:
                x = False
        else:
            print(dialog_error.format(digit))
    return digit

# Функция для ввода даты в формате "%Y-%m-%d" и её проверки на корректность
# В случае некорректного значения повторяет ввод
def input_valid_date(format_date, dialog, dialog_error):
    '''Функция для ввода даты в формате "%Y-%m-%d" и её проверки'''

    x = True
    while x == True:
        date_str = input(dialog)
        if date_str == "":
            date_str = datetime.today().strftime("%Y-%m-%d") 
            x = False
        else:            
            if valid_date(date_str, format_date) == True:
                x = False
            else:
                print(dialog_error.format(date_str))
    return date_str

# Функция для ввода времени в формате "%H:%M" и проверки на корректность
# В случае некорректного значения повторяет ввод
def input_valid_time(format_time, dialog, dialog_error):
    '''Функция для ввода времени в формате "%H:%M" и его проверки'''

    x = True
    while x == True:
        time_str = input(dialog)
        if time_str == "":
            time_str = datetime.today().strftime("%H:%M")
            x = False
        else:
            if valid_time(time_str, format_time) == True:
                x = False
            else:
                print(dialog_error.format(time_str))
    return time_str

# Функция для ввода текстовой строки и проверки лимита её длинны
# В случае превышения лимита повторяет ввод
def input_valid_string(limit, dialog, dialog_error):
    '''Функция для ввода текстовой строки длинной не более limit'''

    x = True
    while x == True:
        note = input(dialog.format(str(limit)))
        if valid_lenstr(note, limit) == True:
           x = False
        else:
            print(dialog_error.format(limit))
    return note
