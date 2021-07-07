#/bin/bash

# Функция проверки являются ли данные числом
# врзвращает TRUE или FALSE
# проверяет:
# * целые положительные и отрицательные числа
# * числа с точкой или запятой
# 2021 Астапчик Михаил
checkDigit(){
if [[ $1 = *[[:digit:]]* ]] && [[ $1 != *[[:space:]]* ]]
then
  return 0
else
  return 1
fi
}

# Пример использования checkDigit
d=123

if checkDigit $d
then
  echo "$var - число"
else
  echo "$var - не число"
fi
