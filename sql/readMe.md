# sql
## Создание демонстрационной базы
+ 1. Скачайте файл с демонстрационной базой данных курса «Основы SQL». Файл называется «sql_foundation» и имеет расширение .sql.

<a href="https://www.dropbox.com/s/i1e3hxmn2b8alju/sql_foundation.sql?dl=1">демонстрационной базой данных курса</a>

+ 2. Загрузите скачанный файл в pgAdmin. Для этого в меню pgAdmin выберите Инструменты->Запросник (в английском вариант Query Tool). В панели инструментов Запросника выберите кнопку открытия файла и в появившемся окне выберите путь к загруженному sql файлу с демонстрационной базой курса.

**! Тут подвох заключаеться он в том, что сначала нужно выбрать картинка 1, а потом открыть запросник иначе не заработает(он будет disabled )**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/1.PNG)

после этого нажимает открыть (иконка папки) и выбираем нужную бд

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/2.PNG)

+ 3. Запустите загруженный файл в pgAgmin. Для этого нажмите на кнопку запуска в панели инструментов Запросника или на клавишу F5.

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/3.PNG)

+ 4. Проверьте правильность выполнения запроса. В нижней части экрана pgAdmin, на закладке «Сообщения» должны появиться результаты выполнения.

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/4.PNG)

Основное, на что нужно обратить внимание — это сообщение «Запрос завершен успешно». Если такое сообщение появилось, значит все хорошо.

Если вы запускаете файл создания демонстрационной базы курса первый раз, то будет выведено несколько Замечаний, что таблицы не существуют. Их можно игнорировать.

Также в левой части интерфейса pgAdmin появится информация о созданных таблицах.

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/5.PNG)

## Запуск SQL запросов в pgAdmin

В pgAdmin для запуска SQL запросов используется уже знакомый нам инструмент Запросник. Давайте откроем окно Запросника и напишем самый первый SQL запрос из видео про Оператор SELECT.

Запрос пишется в среднем окне, закладка Query Editor. Для запуска запроса нажимаем F5 или кнопку Execute в панели инструментов Запросника.

Полученные в ходе выполнения запроса данные показываются в нижней части окна, на закладке «Результат».

**! чтобы сделать запрос надо нажать запросник и в новом окне делать запросы к бд**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/6.PNG)

## 1. Select

```sql
Select * from таблица_название
+ * столбцы_название - можно указывать через запятую.
```

### псевдоним AS
По сути создаёт новую переменную, которая имеет тот же тип данных и те же значения, что и у родителя, ключевое слово **AS**

```sql
SELECT name AS nero_name, appearances FROM superheroes;
```

**! можно пропустить ключевое слово AS и написать через пробел имя_родителя имя_потомка!, например вот так:**

```sql
SELECT name nero_name, appearances FROM superheroes;
```

### Выбор уникальных значений столбцов
Выводит значения, которые не повторяються в столбце, а если повторяеться, то выводит первое в очереди.

SELECT DISTINCT(Название_стобца) FROM superheroes;

```sql
SELECT DISTINCT(align) FROM superheroes;
```
так же можно ещё ограничить с помощью **LIMIT**

```sql
SELECT DISTINCT(hair) FROM superheroes LIMIT 10;
```
 
Если будет меньше результатов, то ничего не случиться, а если больше 10, то выдаст ровно 10. 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/7.PNG)

## 2.  WHERE

ключевое слово **where** указывает какие строки мы хотим выбрать из тиблиц. По сути это фильтр.

```sql
SELECT * FROM superheroes WHERE gender ='Female Characters'
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/8.PNG)

```sql
 SELECT * FROM superheroes WHERE align = 'Reformed Criminals'
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/9.PNG)


Операторы сравнения: 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/10.PNG)

### BETWEEN

Значение находяться в заданом диапазоне

```sql
 SELECT * FROM superheroes WHERE year BETWEEN 2000 AND 2005
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/11.PNG)

значение находиться в некотором списке

### IN
Проверяет наличие в столбце значений(можно задать через запятую)

```sql
SELECT * FROM superheroes WHERE hair IN ('Strawbery Blond Hair','Red Hair', 'Auburn Hair')
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/12.PNG)

### LIKE
+ **%** - любое количество символов (включая 0) **содержит**
+ **_** -ровно одному символу

```sql
SELECT * FROM superheroes WHERE hair LIKE '%Blond%'
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/13.PNG)

### логические операции

+ AND -И 
+ OR -ИЛИ
+ NOT - логическое НЕ

```sql
 SELECT * FROM superheroes WHERE hair ='Red Hair'
 OR hair='Strawbery Blond Hair'
 OR hair='Auburn Hair'
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/14.PNG)


так же можно использовать с **IN**

```sql
SELECT * FROM superheroes WHERE hair NOT IN ('Red Hair', 'Strawbery Blond Hair','Auburn Hair')
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/14.PNG)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/16.PNG)