#/bin/bash

#
# Функция проверки и замены служебных символов для поля формата CSV
#
# Меняем разделитель полей CSV (обычно "," или ";") на другой символ, если есть
# Меняем символ `"` на `'`, если такие есть
# Меняем символ "\n" на "\u000A", если такие есть
# Требует три позиционных параметра:
# $1 - строка поля CSV-файла
# $2 - разделитель полей CSV-файла
# $3 - замена для разделителя полей CSV-файла
# GPLv3 2021 Астапчик Михаил

checkFormatCSV(){
  
  temp=${1//$2/$3}            # меняем разделитель CSV
  temp=${temp//\"/\'}         # меняем двойную кавычку
  temp=${temp//\\n/\\u000A}   # меняем перевод строки
  #temp=${temp//"\n"/"\u000A"}
  echo ${temp}
}

#Пример использования
separatorCSV=";"              # разделитель CSV
sep_replace="\u003B"          # замена для разделителя CSV

CSVfield="vcb;vn\n vn\"hj8"   # пример строки поля CSV

# Сначало выводим первоначальную строку поля CSV
echo "Поле CSV до замены, echo и printf"
echo $CSVfield
printf "$CSVfield\n"

# Выводим строку поля CSV после replaceSymbolsCSV
echo "Поле CSV после замены, echo и printf"
echo $(checkFormatCSV "$CSVfield" $separatorCSV $sep_replace)
printf "$(checkFormatCSV "$CSVfield" $separatorCSV $sep_replace)\n"
