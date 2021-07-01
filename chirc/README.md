# "Чирк". Простой блокнот на Bash

"Чирк" -  очень простой скрипт "Блокнот" для текстовых заметок в csv-файл в формате:
 
    Дата;текст заметки
    
* Диалоговый режим
* Автоматическое добавление даты
* Заметка не более 140 символов
* Поиск через символ "/" в начале ввода.

Имя csv-файла определяется в переменной `file_csv`


## Запись заметки

После запуска скрипта последует предложение для ввода "Черкануть:". После ввода заметки (не более 140 символов) произойдёт запись в файл (по умолчантю `mynotes.csv`) с добавлением текущей даты.

```
~$ ./chirc.sh
Чиркануть: Моя заметка 1
Записано в mynotes.csv
~$ cat mynotes.csv 
06-29-2021;Моя заметка 1
```

## Режим поиска

Если в начале ввода есть символ поиска "/", то введённый текст используется как шаблон для поиска через `grep` в `file_csv`

```
$ ./chirc.sh 
Чиркануть: /заметка 3
07-01-2021;Моя заметка 3
```

**Однострочная версия**

    echo $(date +"%m-%d-%Y")";""Текст заметки" >> mychirics.csv