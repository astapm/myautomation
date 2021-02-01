#! /usr/bin/env python

# GNU GPL v3 2021 Astapchyk Mikhail

# Dice game for command line
# Takes one parameter - the number of dice
# After rolling, dice points are printed to standard output
#
#     $ python3 dicer.py 5
#     3 6 2 5 3
#
# You can choose from 1 to 12 hex dice 

# Игра "Игральные кубики" для командной строки
# Принимает один параметр -- количество кубиков
# После броска очки на кубиках выводится в стандартный вывод
#
#     $ python3 dicer.py 5
#     3 6 2 5 3
#
# Можно выбрать от 1 до 12 шестигранных кубиков


import sys
from random import randint
dice = []
result = ""
if len(sys.argv) > 2:
    num_dices = sys.argv[1]
    if num_dices.isdigit():
        num_dices = int(num_dices)
        if (num_dices < 12):
            for x in range(num_dices):
                point = randint(1,6)
                dice.append(str(point))
        result = " ".join(dice)   
        print(result)
sys.exit()
