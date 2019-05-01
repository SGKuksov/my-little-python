# УПРАЖНЕНИЯ ПО КУРСУ PYTHON. УРОК 10

Создать собственный открытый репозиторий, загрузить на него решение. О том, как это сделать см. статью.

В сумме за упражнения урока можно набрать 57 баллов.

## Упражнение 10.1 (5 баллов из 10)

Напишите программу, выполняющую функции простейшего калькулятора. Программа получает два числа, а затем запрашивает оператор. Обеспечьте корректную обработку ввода, который не преобразуется в числа. Обработайте ошибки деления на ноль.

(ответ в виде файла: my_calc.py)

## Упражнение 10.2 (7 баллов из 10)

В файле [10/ temper.stat](https://github.com/dm-fedorov/python3_intro/blob/master/lesson_10/temper.stat) представлена ежемесячная максимальная температура в градусах по Фаренгейту одного из аэропортов мира в период с 1948 по 2016.

Необходимо определить максимальные и минимальные значения, среднюю температуру.

Определить, сколько уникальных температур содержится в файле.  


(ответ в виде файла: aero_temper.py)

## Упражнение 10.3 (7 баллов из 10)

Напиши программу для очистки и нормализации первой главы ‘Моби Дика’, находящегося в файле [10/ moby.txt](https://github.com/dm-fedorov/python3_intro/blob/master/lesson_10/moby.txt).

Все символы должны относиться к одному регистру. 
Удалить все знаки препинания.
Записать слова по одному на строку во второй файл с именем moby_clean.txt 

(ответ в виде файла: moby.py)


## Упражнение 10.4 (6 баллов из 10)

Прочитайте содержимое файла moby_clean.txt, полученного в упражнении 10.3. Используйте словарь для подсчета вхождений каждого слова, выведите первые 5 самых частых и самых редких слов.

Можно, например, воспользоваться функцией [09/ histogram_v2.py](https://github.com/dm-fedorov/python3_intro/blob/master/lesson_9/histogram_v2.py).

(ответ в виде файла: moby_stat.py)


## Упражнение 10.5 (6 баллов из 10)

Напишите функцию, которая вставляет нумерацию перед строками текстового файла. В функцию необходимо передать имя входного текстового файла и имя выходного текстового файла. 
Например, входной файл имеет имя text.txt и содержит следующий текст:
Край любимый! Сердцу снятся
Скирды солнца в водах лонных,
Я хотел бы затеряться
В зеленях твоих стозвонных.

Имя выходного файла указываем update_text.txt и он будет содержать следующий текст:
1 Край любимый! Сердцу снятся
2 Скирды солнца в водах лонных,
3 Я хотел бы затеряться
4 В зеленях твоих стозвонных.

Корректно обработайте возможность передачи несуществующего файла.

(ответ в виде файла: text_numbers.py)





## Упражнение 10.6 (6 баллов из 10)

Напишите функцию для записи файлов, разделенных запятыми (формат CSV). 
Функция должна получать через параметры имя файла и список кортежей. Кортежи должны содержать name, address и age. 
В итоговом файле должна появиться первая строка заголовка, за которой следует строка для каждого кортежа. 
Если функции будет передан следующий список кортежей:

[(‘Георгий’, ‘Невский проспект’, ’22’), (‘Иван’, ‘пр. Ветеранов’, ’21’)] 

в файл должны быть записаны следующие данные:

name,address,age
Георгий,Невский проспект,22
Иван,пр. Ветеранов,21

Обработайте возможные ошибки при работе с файлами. 

(ответ в виде файла: create_csv_from_list.py)

## Упражнение 10.7 (6 баллов из 10)

Напишите функцию для чтения CSV-файлов. 

В качестве входного аргумента функция принимает имя файла в формате CSV.
Функция должна возвращать список словарей, интерпретируя первую строку файла как имена ключей, а каждую последующую строку как значения этих ключей. 

Для файла с данными:

name,address,age
Георгий,Невский проспект,22
Иван,пр. Ветеранов,21

будет возвращен следующий результат:

[{'name': 'Георгий', 'age': '22', 'address': 'Невский проспект'}, {'name': 'Иван', 'age': '21', 'address': 'пр. Ветеранов'}]

Обработайте возможные ошибки при работе с файлами. 

(ответ в виде файла: read_csv_dict.py)

