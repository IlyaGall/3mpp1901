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

## 3. сортировка в sql:ORDER BY

Нужно, чтобы данные выдавались в определённом порядке. с помощью слова **ORDER BY**

```sql
SELECT * FROM superheroes ORDER BY year
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/17.PNG)

Порядок сортировки (указываться в конце)
+ **ASC** (ascending)-сортировка по возрастанию(по умолчанию)
+ **DESC** (descending) - сортировка по убыванию

```sql
SELECT * FROM superheroes ORDER BY year DESC
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/18.PNG)

+ можно использовать совместно с where

```sql
SELECT * FROM superheroes
 WHERE align='Bad Characters'
ORDER BY appearances DESC
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/19.PNG)

+ сортировка с ограничением

```sql
SELECT * FROM superheroes 
WHERE align='Bad Characters'
AND gender = 'Female Characters'
ORDER BY appearances DESC
LIMIT 5
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/20.PNG)

+ сортировка по нескольким столбцам

```sql
SELECT * FROM superheroes 
ORDER BY year, appearances 
```
сначала сортировка идёт по столбику year, а потом по appearances. Групируеться по году, а потом внутри года по appearances
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/21.PNG)


![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/22.PNG)

## 4. Создание таблиц create table
спомощью ключевого слова  **CREATE TABLE**
```sql
CREATE TABLE Имя таблицы(
    название_столбца type
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/23.PNG)

типы данных 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/24.PNG)



**! NUMERIC -медлено, но точно**  
**! REAL и DOUBLE PRECISION быстро не потеря точности** 


### первичный ключ в таблице

**PRIMARY KEY**  нужен, чтобы отличать записи друг от друга. Он уникален

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/25.PNG)

+ Автоматическое заполнение первичного ключа **SERIAL PRIMARY KEY**. Автоматически увеличивает значение  id при добовлении новых записей

**! AUTO_INCREMENT используется в mySQL**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/26.PNG)

Просмотр данных о созданной таблицы с помощью команды */d название таблицы*

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/27.PNG)

### Удаление таблицы в SQL

**DROP TABLE название таблицы**

Скрипт многоразовый, позволяет заново установить таблицу, если что-то испоритил
сначала пытаеся удалить таблицы если она существует. **IF EXISTS название таблицы;**

```sql
-- Создаём таблицу супергероев
DROP TABLE IF EXISTS superheroes;
CREATE TABLE superheroes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    align VARCHAR(30),
    eye VARCHAR(30),
    hair VARCHAR(30),
    gender VARCHAR(30),
    appearances INT,
    year INT,
    universe VARCHAR(10)
);
```

### Изменение таблиц в SQL
 ключевое слово **ALTER TABLE** (изменение таблицы) 

```ALTER TABLE название_таблицы команда```
+ **ADD COLUMN** название тип_данных
+ **DROP COLUMN** удаление
+ **RENAME COLUMN** переменовать с название **TO** на название
+ **RENAME TO** переменовать всю таблицу

```sql
 ALTER TABLE superheroes ADD COLUMN alive BOOLEAN;
 ALTER TABLE superheroes ADD COLUMN 
 first_appearances TIMESTAMP;
 -- TIMESTAMP месяц и год
ALTER TABLE superheroes DROP COLUMN year;
ALTER TABLE superheroes RENAME COLUMN name TO hero_name;
ALTER TABLE superheroes RENAME TO comic_Characters;
 ```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/28.PNG)

## 5 ВСТАВКА И ИЗМЕНЕНИЕ ДАННЫХ В SQL

**INSERT INTO Название_таблицы(столбец_1, столбец_2, столбец_3....столбец_n)**

```sql
DROP TABLE IF EXISTS superheroes;
CREATE TABLE superheroes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    align VARCHAR(30),
    eye VARCHAR(30),
    hair VARCHAR(30),
    gender VARCHAR(30),
    appearances INT,
    year INT,
    universe VARCHAR(10)
);
-- new code 
INSERT INTO superheroes(name, appearances, universe)
VALUES ('Spider-Man', 4043,'marvel');
SELECT * FROM  superheroes
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/29.PNG)

2 вставка

```sql
INSERT INTO superheroes(name, align, eye, hair,
gender, appearances, year, universe)
VALUES ('Spider-Man (Peter Parker)', 'Good
Characters', 'Hazel Eyes', 'Brown Hair',
'Male Characters', 4043, 1962, 'marvel') 
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/30.PNG)

3 вид вставики вставка(лучше так не вставлять)

```sql
INSERT INTO superheroes
VALUES (1, 'Spider-Man (Peter Parker)', 'Good
Characters', 'Hazel Eyes', 'Brown Hair’,
'Male Characters', 4043, 1962, 'marvel')
```

### ИЗМЕНЕНИЕ ДАННЫХ В ТАБЛИЦЕ

```sql
**UPDATE название_таблицы 
SET Название_стобца=значение,
Название_стобца=значение
...
WHERE id=1
```


```sql
UPDATE superheroes
SET name='Batman',
universe='dc'
WHERE id=1
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/31.PNG)

Второй вариант, но лучше использовать id
```sql
UPDATE superheroes
SET gender='Man',
WHERE gender='Male Characters'
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/32.PNG)

### УДАЛЕНИЕ ДАННЫХ ИЗ ТАБЛИЦЫ

```sql
DELETE FROM superheroes
WHERE id=2
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/33.PNG)

множественное удаление

```sql
DELETE FROM superheroes
WHERE gender='Male Characters'
```

**! УДАЛЕНИЕ ВСЕХ ДАННЫХ**

```sql 
DELETE FROM superheroes
```

### ИТОГ

Вставка данных в таблицы
+ Оператор INSERT
Изменение данных в таблице
+ Оператор UPDATE
Удаление данных из таблиц
+ Оператор DELETE
Особенности
+ Один оператор может менять несколько строк данных Фильтры в WHERE такие же, как в SELECT Первичный ключ позволяет однозначно идентифицировать строки

## 6 ГРУППИРОВКА ДАННЫХ В SQL: GROUP BY

```sql
SELECT Название_столбца, что делаем FROM название_таблицы
GROUP BY по_какому_столбцу
```
+  COUNT(*) -выполняет подсчёт строк
```sql
SELECT gender, COUNT(*) FROM superheroes
GROUP BY gender
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/34.PNG)

2 запрос
```sql
SELECT align, COUNT(*) FROM superheroes
GROUP BY align
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/35.PNG)

### МНОГОУРОВНЕВАЯ ГРУППИРОВКА ДАННЫХ В SQL

```sql
SELECT universe, align, COUNT(*) FROM superheroes
GROUP BY universe, align
```
КОЛИЧЕСТВО СУПЕРГЕРОЕВ РАЗНЫХ ТИПОВ

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/36.PNG)

### ФИЛЬТРАЦИЯ И ГРУППИРОВКА ДАННЫХ В SQL

```sql
SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
```

КОЛИЧЕСТВО СУПЕРГЕРОЕВ ПО ЦВЕТУ ВОЛОС

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/37.PNG)

### ФИЛЬТРАЦИЯ, ГРУППИРОВКА И СОРТИРОВКА

```sql
SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
ORDER BY count(*) DESC
```
КОЛИЧЕСТВО СУПЕРГЕРОЕВ ПО ЦВЕТУ ВОЛОС

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/38.PNG)

### ФИЛЬТРАЦИЯ, ГРУППИРОВКА, СОРТИРОВКА И ЛИМИТ

```sql
SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
ORDER BY count(*) DESC
LIMIT 5
```
ТОП 5 ЦВЕТОВ ВОЛОС У СУПЕРГЕРОЕВ ЖЕНЩИН

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/39.PNG)

### ИТОГИ
Группировка данных
+ Ключевое слово GROUP BY
+ Группировка по одному или нескольким столбцам
Агрегатные функции
+ COUNT, SUM, AVG, MAX, MIN
 Группировка и другие возможности SELECT
+ Фильтрация: WHERE
+ Сортировка: ORDER BY
+ Ограничение количества строк: LIMIT

## 7 АГРЕГАТНЫЕ ФУНКЦИИ В SQL

вместе GROUP BY 
```sql
SELECT align, COUNT(*) FROM superheroes
GROUP BY align
```
АГРЕГАТНЫЕ ФУНКЦИИ В SQL

+ AVG Среднее значение
+ COUNT Количество значений
+ MAX Максимальное значение
+ MIN Минимальное значение
+ SUM Сумма

пример

```sql
SELECT align, COUNT(*), SUM(appearances)
FROM superheroes
GROUP BY align
```
2 всего героев 3 всего появлялись
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/40.PNG)



### AVG SUN
использованние AS

```sql
SELECT align, AVG(appearances),
SUM(appearances)/COUNT(*) AS average
FROM superheroes
GROUP BY align
```
сколько раз в средним появляються супергероии

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/41.PNG)

### агрегатными ф-ми min/max
```sql
SELECT year, MIN(appearances), MAX(appearances)
FROM superheroes
GROUP BY year
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/42.PNG)


## сортировка данных в запросах с агрегатными ф-ми
```sql
SELECT year, MIN(appearances), MAX(appearances)
FROM superheroes
GROUP BY year
ORDER BY year
```

наименее популярный и наиболее популярный герой 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/43.PNG)


```sql
SELECT year, MIN(appearances), MAX(appearances)
FROM superheroes
GROUP BY year
ORDER BY MAX(appearances) DESC
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/44.PNG)

```sql
SELECT year, MIN(appearances),
MAX(appearances) AS max_ap
FROM superheroes
GROUP BY year
ORDER BY max_ap DESC
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/45.PNG)

## LIMIT в запросах с агригатными ф-ми
```sql
SELECT year, MIN(appearances),
    MAX(appearances) AS max_ap
FROM superheroes
GROUP BY year
ORDER BY max_ap DESC
LIMIT 5
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/46.PNG)

## агрегатные ф-и без группировки

```sql
SELECT COUNT(*),
    MIN(appearances),
    MAX(appearances),
    SUM(appearances),
    AVG(appearances)
FROM superheroes
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/47.PNG)


## ИТОГ
Агрегатные функции
+ Обрабатывают несколько строк и вычисляют одно значение
+ Используются совместно с группировкой
Распространенные агрегатные функции
+ AVG, COUNT, MAX, MIN, SUM
+ Серверы баз данных поддерживают дополнительные функции
Агрегатные функции и другие возможности SELECT
+ Фильтрация (WHERE), сортировка (ORDER BY), ограничение количества строк (LIMIT)
+ Фильтрация результатов группировки: HAVING

## 8 ГРУППИРОВКА И ФИЛЬТРАЦИЯ В SQL: HAVING

во время работы Where группы ещё не созданы, поэтому после where нельзя использовать группироваку, можно только having c агригатными ф-ит.
Having работает после создания групп
```sql
SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
HAVING COUNT(*) > 10
```
без having

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/48.PNG)

c having

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/49.PNG)


```sql
SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
HAVING COUNT(*) BETWEEN 50 AND 300
```
количество строк больше 50, но меньше 300

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/50.PNG)

## ИТОГИ
Фильтрация данных
+ WHERE – фильтрация строк в таблице
+ HAVING – фильтрация результатов группировки
Порядок выполнения SELECT
+ Выбор таблицы: FROM
+ Фильтрация строк из таблицы: WHERE
+ Группировка: GROUP BY
+ Фильтрация результатов группировки: HAVING

## 9 ДЕКОМПОЗИЦИЯ ДАННЫХ В БАЗЕ

когда несколько бд. Между ними нужна связь. И чтобы её установить нужно добавить сылку на id из главной таблицы Foregin key

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/51.PNG)

если много копий одной строки или, если, например, мы удалил запись Reformed Criminals(перевоспитанные преступники), то потеряем эти данные и не будем занать, что такая запись вообще возможна

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/52.PNG)

для решения этой проблемы надо делать следующие:

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/53.PNG)

создаётся отдельная внешняя таблица , в которой будет содержаться информация

**! По сути это компромис между правильностью и понятностью бд**

## ИТОГ
Несколько таблиц в базе данных
+ Разные сущности
+ Декомпозиция одной таблицы на несколько
Связи между таблицами
+ Ссылки из одной таблицы на другую
+ Внешний ключ (FOREIGN KEY
Проектирование баз данных
+ Нормализация: нормальные формы
+ Типы связей: один к одному, один ко многим, многие ко многим

## 10 ЗАПРОС ДАННЫХ ИЗ НЕСКОЛЬКИХ ТАБЛИЦ
БАЗА ДАННЫХ ОНЛАЙН-ШКОЛЫ

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/54.PNG)

## ОБЪЕДИНЕНИЕ ДАННЫХ ИЗ НЕСКОЛЬКИХ ТАБЛИЦ В SELECT

```sql
SELECT products.name(столбец), product_types.type_name(столбец)
FROM таблица_1 JOIN таблица_2
ON products.type_id(ключ) = product_types.id(внешний ключ)
```

```sql
SELECT products.name, product_types.type_name
FROM products JOIN product_types
ON products.type_id = product_types.id
```
получили
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/55.PNG)

### ПСЕВДОНИМЫ СТОЛБЦОВ
```sql
SELECT p.name AS product_name,
t.type_name AS product_type,
p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/56.PNG)

### ФИЛЬТРАЦИЯ ДАННЫХ ИЗ НЕСКОЛЬКИХ ТАБЛИЦ

```sql
SELECT p.name AS product_name,
t.type_name AS product_type,
p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
WHERE t.type_name='Онлайн-курс'
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/57.PNG)


## ФИЛЬТРАЦИЯ ДАННЫХ ИЗ НЕСКОЛЬКИХ ТАБЛИЦ
```sql
SELECT p.name AS product_name,
t.type_name AS product_type,
p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
WHERE t.type_name = 'Вебинар'
AND p.price = 0
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/58.PNG)

## СОРТИРОВКА ДАННЫХ ИЗ НЕСКОЛЬКИХ ТАБЛИЦ
```sql
SELECT p.name AS product_name,
    t.type_name AS product_type,
    p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
WHERE t.type_name='Онлайн-курс'
ORDER BY p.price DESC
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/59.PNG)

## ИТОГ
Запрос данных их нескольких таблиц
+ Оператор SELECT
+ В ключевом слове FROM указываем несколько таблиц с JOIN
+ После ключевого слова ON указываем условия объединения
Связи между таблицами
+ Ссылки из одной таблицы на другую
+ Внешний ключ (FOREIGN KEY)
Использование JOIN в SELECT
+ Комбинация с WHERE, ORDER BY, LIMIT, GROUP BY, HAVING
+ Типы JOIN: внешнее и внутреннее, левое и правое, перекрестное, полное

## 11 ТИПЫ JOIN В SQL

### ВНУТРЕННЕЕ ОБЪЕДИНЕНИЕ(по умолчанию)
Строки, в которых были найдены другие строки **INNER JOIN** можно не писать
```sql
SELECT products.name, product_types.type_name
FROM products JOIN product_types
ON products.type_id = product_types.id
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/60.PNG)

### ВНЕШНЕЕ ОБЪЕДИНЕНИЕ
чтобы попадали строки, которых нет пары

+ ЛЕВОЕ ВНЕШНЕЕ ОБЪЕДИНЕНИЕ **LEFT OUTER JOIN**

```sql
SELECT products.name, product_types.type_name
FROM products LEFT OUTER JOIN product_types
ON products.type_id = product_types.id
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/61.PNG)

результат

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/62.PNG)

+ ПРАВОЕ ВНЕШНЕЕ ОБЪЕДИНЕНИЕ **RIGHT OUTER JOIN**

```sql
SELECT products.name, product_types.type_name
FROM products RIGHT OUTER JOIN product_types
ON products.type_id = product_types.id
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/61.PNG)

результат
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/63.PNG)


**! суть в том, что если левое, то включаются всё столбцы из левой таблицы, даже те у которых нет пары, а из правой, только те значение которые имеют пару с левой**
**! суть в том, что если правое, то включаются всё столбцы из правой таблицы, даже те у которых нет пары, а из левой, только те значение которые имеют пару с правой**

+ПОЛНОЕ ВНЕШНЕЕ ОБЪЕДИНЕНИЕ 

```sql
SELECT products.name, product_types.type_name
FROM products FULL OUTER JOIN product_types
ON products.type_id = product_types.id
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/61.PNG)

результат
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/64.PNG)

+ ПЕРЕКРЕСТНОЕ ОБЪЕДИНЕНИЕ

каждый с каждым
```
SELECT products.name, product_types.type_name
FROM products CROSS JOIN product_types
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/61.PNG)

результат

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/65.PNG)

## ИТОГ

Внутренне объединение
+ INNER JOIN- Тип объединения по умолчанию
Внешнее объединение
+ Левое – LEFT OUTER JOIN
+ Правое – RIGHT OUTER JOIN
+ Полное – FULL OUTER JOIN
Перекрестное объединение
+ CROSS JOIN- Не используется на практике

## 12 Схема базы данных (презентация, схема базы данных онлайн-школы в DrawSQL).

Графическое представление бд
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/66.PNG)

ПРОДУКТЫ В ЗАКАЗЕ

```sql
SELECT p.id,
    p.name,
    p.price,
    s.quantity,
    p.price * s.quantity AS total
FROM products AS p JOIN sales AS s
ON p.id = s.product_id
WHERE s.order_id=2
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/67.PNG)

ВСЕ ПОКУПКИ ЗАКАЗЧИКА
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/66.PNG)

```sql
SELECT p.id,
    p.name,
    p.price,
    s.quantity,
    p.price * s.quantity AS total
FROM products AS p JOIN sales AS s
    ON p.id = s.product_id
    JOIN orders AS o
    ON o.id = s.order_id
WHERE o.customer_id=1
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/68.PNG)

ИТОГИ
Схема базы данных
+ Таблицы
+ Столбцы в таблицах и типы данных в них
+ Связи между таблицами

Типы связей между таблицами
+ Один к одному (one-to-one)
+ Один ко многим (one-to-many)
+ Многие к одному (many-to-one)
+ Многие ко многим (many-to-many, реализуется через отдельную таблицу)

## 13 ПОДЗАПРОСЫ В SQL
Подзапрос выполняеться всёгда первым
```sql
SELECT id, name, price
FROM products
--WHERE price = (SELECT MAX(price)
 --       FROM products)
```
без подзапроса

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/69.PNG)

### ВЫВЕСТИ ИНФОРМАЦИЮ О САМОМ ДОРОГОМ ПРОДУКТЕ
```sql
SELECT id, name, price
FROM products
WHERE price = (SELECT MAX(price)
        FROM products)
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/70.PNG)

### ВЫВЕСТИ ИНФОРМАЦИЮ О ПРОДУКТАХ, КОТОРЫЕ БЫЛИ ПРОДАНЫ ХОТЯ БЫ ОДИН РАЗ

```sql
SELECT id, name, price
FROM products
WHERE id IN (SELECT product_id
FROM sales)
```

Тут **IN** потому, что тут есть список

```SELECT product_id FROM sales```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/71.PNG)

весь скрипт

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/72.PNG)

### ПОДЗАПРОСЫ В UPDATE 
Увеличить стоимость каждой книги на 500р
```sql  
UPDATE products
SET price = price + 500
WHERE type_id = (SELECT id
        FROM product_types
        WHERE type_name='Книга')
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/73.PNG)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/74.PNG)

## ИТОГ
Подзапросы в SQL (subqueries)
+ Запрос внутри другого запроса SQL
+ Оформляется в круглых скобках
+ Запускается перед основным запросом
Диагностика подзапроса
+ Запуск подзапроса отдельно от основного запроса
Использование подзапросов в командах SQL
+ SELECT
+ UPDATE
+ DELETE
+ INSERT

## 14 ТРАНЗАКЦИИ В БАЗАХ ДАННЫХ

ПРИЧИНЫ НЕВЫПОЛНЕНИЯ КОМАНД

Отказ СУБД
+ Аппаратная проблема с сервером СУБД
+ Программная ошибка в СУБД или операционной системе
+ Не хватает места на диске для записи данных
Отказ приложения пользователя
+ Аппаратная проблема на клиенте
+ Программная ошибка в приложении или операционной системе
+ Пользователь прервал работу приложения 
Потеря сетевого соединения клиента и сервера СУБД
+ Аппаратная проблема с сетевым оборудованием на клиенте/сервере
+ Проблемы с работой сети

**Транзакция** – последовательность команд SQL, которые должны быть
выполнены полностью или не выполнены вообще.

```sql
UPDATE accounts SET balance = balance – 15000
WHERE account_number = 1234567 -- клиент онлайн школы

UPDATE accounts SET balance = balance + 15000
WHERE account_number = 9876543 -- онлайн школа
```

**НАЧАЛО ТРАНЗАКЦИИ**
```START TRANSACTION;```

### ВЫПОЛНЕНИЕ ТРАНЗАКЦИИ
```sql
START TRANSACTION;

UPDATE accounts SET balance = balance – 15000
WHERE account_number = 1234567;
UPDATE accounts SET balance = balance + 15000
WHERE account_number = 9876543; 
```

### ФИКСАЦИЯ ТРАНЗАКЦИИ COMMIT

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance – 15000
WHERE account_number = 1234567;

UPDATE accounts SET balance = balance + 15000
WHERE account_number = 9876543;

COMMIT;
```

```COMMIT``` - записать изменения в бд

### ОТКАТ ТРАНЗАКЦИИ ROLLBACK

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance – 15000
WHERE account_number = 1234567;

UPDATE accounts SET balance = balance + 15000
WHERE account_number = 9876543;

ROLLBACK;

```

### АВТОМАТИЧЕСКАЯ ФИКСАЦИЯ ТРАНЗАКЦИЙ

+ Специальный режим работы СУБД
+ После выполнения каждой команды SQL автоматически фиксируется транзакция
+ Нет возможности отменить изменения

Использование режима автоматической фиксации транзакций
+ PostgreSQL – включено по умолчанию
+ Oracle – выключено по умолчанию

### ЗАВЕРШЕНИЕ ТРАНЗАКЦИЙ
+ Команды **COMMIT** или **ROLLBACK** - Явное подтверждение или отмена транзакции
+ **Запуск команд создания, изменения или удаления таблиц** 
    + Создание, изменение или удаление таблицы не может быть отменено
    + Перед запуском команды предыдущая транзакция фиксируется
+ Сбой сервера СУБД
    + Откат всех незавершенных транзакций после восстановления сервера
+ Сбой клиента СУБД
    + Откат незавершенной транзакции после тайм-аута

### ИТОГ
Транзакции в базах данных
+ Последовательность команд, которые должны быть выполнены все
+ полностью, или не выполнены совсем

Начало транзакции
+ Команда START TRANSACTION
+ Автоматическая фиксация транзакций
Завершение транзакции
+ Команда COMMIT – фиксация транзакции
+ Команда ROLLBACK – откат транзакции

## 15 ИНДЕКСЫ В БАЗАХ ДАННЫХ

Позволяет увеличить скорость поиска данных

Индексы
+ Структура данных, позволяющая быстро определить положение интересующих данных в базе
+ Создается для столбца (совокупности столбцов) в таблице
+ Обеспечивает возможность повысить производительность запросов

Использование индексов
+ Быстрый поиск положения интересующих данных в таблице
+ Извлечение всех интересующих данных из таблицы по найденному положению
+ Реализуется автоматически СУБД

### СОЗДАНИЕ ИНДЕКСА

```sql
CREATE INDEX superheroes_name_idx
ON superheroes(name)
```

при использовании индекса не надо менять sql запрос

### КОГДА МОЖЕТ ИСПОЛЬЗОВАТЬСЯ ИНДЕКС

Фильтрация данных из таблицы
+ Для столбца, указанного в WHERE, существует индекс

Объединение данных
+ Для столбцов, указанных в условии объединения, существует индекс

Сортировка данных
+ Для столбцов, указанных в ORDER BY, существует индекс в правильной последовательности сортировки

### ПОРЯДОК СОРТИРОВКИ ДАННЫХ В ИНДЕКС

```sql
CREATE INDEX superheroes_appearances_idx
ON superheroes(appearances DESC)
```


### ИНДЕКС ПО НЕСКОЛЬКИМ СТОЛБЦАМ
```sql
CREATE INDEX person_name_idx
ON person(last_name, first_name)
```

### УДАЛЕНИЕ ИНДЕКСА

```DROP INDEX person_name_idx```


### НЕДОСТАТКИ ИНДЕКСОВ
+ Изменения в базе данных
+ Изменение в исходной таблице приводит к необходимости изменять все
+ связанные с ней индексы
+ Снижение производительности
+ Если индексов много, то при изменении данных в таблице требуется длительное временя для обновления индексов



### ИТОГ
Индекс
+ Структура данных, позволяющая быстро определить положение интересующих данных в базе
+ Создается для столбца или нескольких столбцов в таблице
Применение индекса
+ Индекс используется автоматически СУБД, если это эффективно
+ Возможности использования: фильтрация, объединение данных из нескольких таблиц, сортировка 
Эффекты от индексов
+ Повышение производительности запросов на чтение
+ Снижение производительности записи данных в таблицу

## 16  ОГРАНИЧЕНИЯ В БАЗАХ ДАННЫХ
### 16.1 id 
```id INT PRIMARY KEY```
### 16.2 НЕПУСТЫЕ ЗНАЧЕНИЯ NOT NULL

```sql
CREATE TABLE superheroes(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL, -- NOT NULL
    align VARCHAR(30),
    eye VARCHAR(30),
    hair VARCHAR(30),
    gender VARCHAR(30),
    appearances INT,
    year INT,
    universe VARCHAR(10)
)
```

### 16.3 УНИКАЛЬНЫЕ ЗНАЧЕНИЯ UNIQUE

```sql
CREATE TABLE superheroes(
    id INT PRIMARY KEY,
    name VARCHAR(100) UNIQUE, -- 
    align VARCHAR(30),
    eye VARCHAR(30),
    hair VARCHAR(30),
    gender VARCHAR(30),
    appearances INT,
    year INT,
    universe VARCHAR(10)
)
```

### 16.4 объеденение ограничений UNIQUE NOT NULL

```sql
CREATE TABLE superheroes(
    id INT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    align VARCHAR(30),
    eye VARCHAR(30),
    hair VARCHAR(30),
    gender VARCHAR(30),
    appearances INT,
    year INT,
    universe VARCHAR(10)
)
```
### 16.5 ПЕРВИЧНЫЙ КЛЮЧ ИЗ НЕСКОЛЬКИХ ПОЛЕЙ
```SQL
CREATE TABLE sales(
    product_id INT,
    order_id INT,
    quantity INT,
PRIMARY KEY(product_id, order_id)
)
```


### 16.6 ОГРАНИЧЕНИЯ ПО ПРОВЕРКЕ ЗНАЧЕНИЙ CHECK

+ **price INT CHECK (price >= 0)** , например цена должна быть больше нуля

```SQL
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT,
price INT CHECK (price >= 0)
)
```
### 16.7 ИМЕНОВАННЫЕ ОГРАНИЧЕНИЯ
можно задать имя
```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT,
    price INT CONSTRAINT positive_price
        CHECK (price >= 0)
)
```
### 16.8 ОГРАНИЧЕНИЯ НА УРОВНЕ ТАБЛИЦЫ

```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT,
    price INT,
CONSTRAINT positive_price CHECK (price >= 0)
)
```
### 16.9 ОГРАНИЧЕНИЯ ССЫЛОЧНОЙ ЦЕЛОСТНОСТИ (Ограничение внешнего ключа)

```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT REFERENCES product_types(id),
    price INT
)
```

### 19.9.1  ДЕЙСТВИЯ ПРИ УДАЛЕНИИ

#### ON DELETE RESTRICT
не даст удалить если есть связанные данные

```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT REFERENCES product_types(id)
    ON DELETE RESTRICT,
    price INT
)
```

#### DELETE CASCADE
Данные будут удаленны каскадно 

```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT REFERENCES product_types(id)
    ON DELETE CASCADE,
    price INT
)
```
### 19.10 ДЕЙСТВИЯ ПРИ ИЗМЕНЕНИИ

#### ON UPDATE RESTRICT 
запрещение изменять строки на которых есть ссылки
```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT REFERENCES product_types(id)
    ON UPDATE RESTRICT,
    price INT
)
```

#### ON UPDATE CASCADE
В случаи изменения строки изменить и каскад
```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT REFERENCES product_types(id)
    ON UPDATE CASCADE,
    price INT
)
```

### 19.20 ВНЕШНИЙ КЛЮЧ НА УРОВНЕ ТАБЛИЦЫ

```sql
CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT,
    price INT,
    FOREIGN KEY(type_id) REFERENCES product_types(id)
)
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/66.PNG)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/75.PNG)

### 

```sql
ПЕРВИЧНЫЙ И ВНЕШНИЙ КЛЮЧИ
CREATE TABLE sales(
    product_id INT REFERENCES products(id),
    order_id INT REFERENCES orders(id),
    quantity INT,
    PRIMARY KEY(product_id, order_id)
)
```

### ИТОГИ
Ограничения
+ Ограничения на выполнение операций с целью сохранения согласованности данных в базе
Типы ограничений
+ Первичный ключ – PRIMARY KEY
+ Внешний ключ – FOREIGN KEY
+ Непустые значения – NOT NULL
+ Уникальные значение – UNIQUE
+ Проверка условий – CHECK


## 17 ПРЕДСТАВЛЕНИЯ В SQL
Создание виртуальной таблицы
```sql
CREATE VIEW customers_v id, name
AS SELECT id, name FROM customers
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/76.PNG)


### ЗАПРОСЫ К ПРЕДСТАВЛЕНИЯМ

```SELECT * FROM customers_v```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/77.PNG)

### ПРЕДСТАВЛЕНИЯ С ДАННЫМИ ИЗ НЕСКОЛЬКИХ ТАБЛИЦ

```sql
CREATE VIEW products_v
AS SELECT p.id AS id,
    p.name AS product_name,
    t.type_name AS product_type,
    p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
```


![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/sql/images/78.PNG)

### ЗАЧЕМ ИСПОЛЬЗОВАТЬ ПРЕДСТАВЛЕНИЯ
Ограничение доступа к данным
+ Представление содержит не все столбцы/строки исходной таблицы
Псевдонимы для сложных запросов
+ Запрос извлекает данные из нескольких таблиц
+ Запрос выполняет группировки и расчет агрегаций
Сокрытие реализации
+ Пользователи работают только с представлениями
+ Таблицы в базе данных можно менять

## МАТЕРИАЛИЗОВАННЫЕ ПРЕДСТАВЛЕНИЯ
Для запросов которые работают довольно долго или часто

```sql
CREATE MATERIALIZED VIEW products_v
AS SELECT p.id AS id,
    p.name AS product_name,
    t.type_name AS product_type,
    p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
```

### ОБНОВЛЕНИЕ МАТЕРИАЛИЗОВАННЫХ ПРЕДСТАВЛЕНИЙ
Данные автоматически не обновляються, поэтому нужно в ручную это делать

```REFRESH MATERIALIZED VIEW products_v```

### УДАЛЕНИЕ ПРЕДСТАВЛЕНИЙ
**DROP VIEW products_v**

### УДАЛЕНИЕ МАТЕРИАЛИЗОВАННЫХ ПРЕДСТАВЛЕНИЙ
**DROP MATERIALIZED VIEW products_v**

ИТОГИ
Представления
+ Псевдонимы для запросов SELECT
+ Используются как аналоги таблиц
+ Не содержат данных 
Использование представлений
+ Ограничение доступа к данным
+ Псевдонимы для сложных запросов
+ Сокрытие реализации
Материализованные представления
+ Содержат данные
+ Повышают скорость выполнения запросов