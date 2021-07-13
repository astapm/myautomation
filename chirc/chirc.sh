#/bin/bash

# Скрипт "Чирк" для записи текстовых заметок в csv-файл:
 #     Дата;текст заметки
 # Диалоговый режим
 # Автоматическое добавление даты
 # Заметка автоматически берётся в кавычки
 # Замена символов сепаратора CSV на `\u003B` и `"` на `'`
 # Заметка не более 140 символов
 # Режим поиска через символ "/" в начале ввода
 # версия 0.6.0 GPLv3, 2021, Михаил Астапчик

# Функция проверки и замены служебных символов для поля формата CSV
 # Меняет разделитель полей CSV (обычно "," или ";") на другой символ
 # Меняет символ `"` на `'`, если есть
 # Меняет символ "\n" на "\u000A"
 # Требует три позиционных параметра:
 # $1 - строка поля CSV-файла
 # $2 - разделитель полей CSV-файла
 # $3 - замена для разделителя полей CSV-файла
 #     checkFormatCSV полеCSV разделительCSV замена_разделителя
checkFormatCSV(){  
  temp=${1//$2/$3}            # меняем разделитель CSV
  temp=${temp//\"/\'}         # меняем двойную кавычку
  temp=${temp//\n/\\u000A}    # меняем перевод строки
  echo ${temp}
}

# Переменные скрипта
 # Имя файла csv
file_csv="mynotes.csv"
 # Разделитель CSV
sep=";"
 # замена для разделителя CSV
sep_replace="\u003B"          

# Для начала выводим небольшую статистику о заметках
if [[ -e $file_csv ]]
then
lines=$(wc -l < $file_csv)
echo "Кол-во заметок: $lines"
fi

# Читаем ввод не более 140 символов
read -e -n 140 -p "Чиркануть: " note

# Есои заметка пустая, то выходим
if [[ $note == "" ]]
then
  exit
fi

# Если в начале ввода есть символ поиска "/"
# то ищем введённый текст через `grep` в `file_csv`
if [[ ${note:0:1} == "/" ]]
then
  grep -i -n "${note:1}" $file_csv
# Если в начале ввода есть команда удаления ":del"
# то удвляется последняя строчка через `sed` в `file_csv`
elif [[ ${note:0:4} == ":del" ]]
then
  sed -i '$d' $file_csv
# Или записываем введённый текст в файл csv,
# добавляя текущую дату
else
  # заменяем в заметке, если есть
  #  - разелитель `$sep` на `\u003B`
  #  - `"` на `'`
  #  - `\n` на `\u000A`
  note=$(checkFormatCSV "$note" $sep $sep_replace)
  # Записываем строку в файл
  echo -n $(date +"%Y-%m-%d")$sep >> $file_csv
  echo "\"$note\"" >> $file_csv
  echo "Записано в $file_csv"
fi
exit

# Подключение git

