# тестировании функций
+ создаём папку ```tests```
+ название тестовой ф-и начинается с ```test_```название ф-и_fun

создали папку и ф-ю, затем импортируем ф-ю

```python
from My_funcs.solution import division

```

далее добовляет

```python
from My_funcs.solution import division


def test_division_good():
    assert division(10, 2) == 5
   ```
+ ```assert``` если будет ```true```, то событие произоёдет, а если ```false```, упадёт

далее переходим в утилиты 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/1.JPG)

нажимаем edit configuration

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/2.JPG)

не забыть добавить 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/3.JPG)

запускаю тест

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/4.JPG)

далее изменим код, добавив ещё один тест

```python
from My_funcs.solution import division


def test_division_good():
    assert division(10, 2) == 5


def test_division_one_more():
    assert division(10, 5) == 2
```
получили следующий результат:

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/5.JPG)

Но писать каждый раз ф-ю не есть хорошо. Поэтому пишем надо использовать ```@pytest.mark.parametrize```

```python
from My_funcs.solution import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result
```
получил следующий результат

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/6.JPG)

## спровоцированная ошибка и проверка на срабатывание
добавим следующий код 
```python

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
```
так как делить на 0 нельзя, то тест должен провалится и выдасть ошибку, но благодаря строчке 
```with pytest.raises(ZeroDivisionError):``` мы сможем узнать провалился ли тест без вывода ошибки. Если тест не провалится, то тут как раз произойдёт ошибка

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/7.JPG)

изменю код, чтобы ошибки не было, но из-за строчки ```with pytest.raises(ZeroDivisionError):``` тест провалится из-за того, что как раз нет ошибки деления на 0
```python

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 1)
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/8.JPG)

можно поймать на ошибку типов

```python
from My_funcs.solution import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [
    (10, 2, 5),
    (20, 10, 2),
    (30, -3, -10),
    (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


def test_type_error():
    with pytest.raises(TypeError):
        division(10, "2")

```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/9.JPG)

подкоректируем код 

```python
rom solution import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [
    (10, 2, 5),
    (20, 10, 2),
    (30, -3, -10),
    (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

@pytest.mark.parametrize("exepected_exception, devisionable, divider",[
    (ZeroDivisionError, 10, 0),
    (TypeError, 20, "2")
])
def test_division_with_error(exepected_exception, devisionable, divider):
    with pytest.raises(exepected_exception):
        division(devisionable, divider)
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/10.JPG)

## 2 часть

создам папку ``My_funcs`` и туда перенесу ```solution``` и там же создам файл ```file_worker.py```, а так же создам файл
```prodfile.txt```

file_worker:
```python
def read_from_file(filepath):
    with open(filepath, "r") as f_o:
        return f_o.readlines()
## print(read_from_file("prodfile.txt"))  для проверки работоспособности
```
prodfile.txt:
```txt
one
two
three
```

продублируем файл ```prodfile.txt```  в ```tests->testfile.txt```

и создадим ещё один тестовый файл ```test_file_workers```
```python
from My_funcs.file_workers import read_from_file


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file("tests/testfile.txt")


```

нажав на 


можно теперь увидеть какие тесты прошли и с каким набором данных, а какие нет

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/11.JPG)

**чтобы гонялся только определённый тест, надо изменить конфиг**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/12.JPG)

подправил код

```python
from My_funcs.file_workers import read_from_file

def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file("testfile.txt")
```

запуск

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/13.JPG)

допустим у нас в тесте есть 2 ф-и, но надо чтобы гонялся один файл, то тогда надо

```python
from My_funcs.file_workers import read_from_file

def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file("testfile.txt")
def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file("testfile.txt")
```

тогда в файл конфигурации теста надо указать ``путь::название ф-и теста``

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/14.JPG)

изменим файл конфигурации обратно(без ::), а так же изменим код теста

```python
from My_funcs.file_workers import read_from_file

def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    with open("testfile.txt", "a") as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file("testfile.txt")

def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n']
    with open("testfile.txt", "a") as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file("testfile.txt")
```

при тесте у нас возникает ошибка из-за того, что всё время добовляеются данные в файл и чтобы зачистить файл
надо написать следующие строки:
```python
    with open("testfile.txt", "w"):
        pass # затирает файл
```
получится вот так

```python
from My_funcs.file_workers import read_from_file


def test_read_from_file():
    with open("testfile.txt", "w"):
        pass # затирает файл
    test_data = ['one\n', 'two\n', 'three\n']
    with open("testfile.txt", "a") as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file("testfile.txt")

def test_read_from_file2():
    with open("testfile.txt", "w"):
        pass # затирает файл
    test_data = ['one\n', 'two\n', 'three\n']
    with open("testfile.txt", "a") as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file("testfile.txt")

```
но каждый тест писать стираение из файла не правильно, поэтому надо создать файл конфигурации в котором будет логика стирания

```conftest.py```

```python
import pytest
@pytest.fixture(autouse=True)

def clean_text_file():
    with open("testfile.txt", "w"):
        pass  # затирает файл
```
перед запуском каждого теста будет выполнятся следующий код благодаря строчке ```@pytest.fixture(autouse=True)```

но проблема в том, что этот код выполнятся всегда. Для любых тестов. Чтобы этого избежать создадим ещё одну директорию

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/debug_code/img_readMe/15.JPG)

и теперь мы избавились от проблемы