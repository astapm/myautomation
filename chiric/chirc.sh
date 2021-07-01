#/bin/bash

# Скрипт "Чирк" для записи текстовых заметок в csv-файл:
#     Дата;текст заметки
# Диалоговый режим
# Автоматическое добавление даты
# Заметка не более 140 символов
# версия 0.1, GPLv3, 2021, Михаил Астапчик

# Имя файла csv
file_csv="mynotes.csv"

# Разделитель csv
sep=";"

# Читаем ввод не более 140 символов
read -n 140 -p "Чиркануть: " note

# Есои заметка не пустая, записываем в файл дату и заметку
if [[ $note != "" ]]
then
  echo -n $(date +"%m-%d-%Y")$sep >> $file_csv
  echo $note >> $file_csv
  echo "Записано в $file_csv"
else
  exit
fi
