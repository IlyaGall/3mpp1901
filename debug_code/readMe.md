# тестировании функций
+ создаём папку ```tests```
+ название тестовой ф-и начинается с ```test_```название ф-и_fun

создали папку и ф-ю, затем импортируем ф-ю 

```python
from solution import division

```

далее добовляет

```python
from solution import division

def test_division_good():
    assert division(10, 2) == 5
   ```
+ ```assert``` если будет ```true```, то событие произоёдет, а если ```false```, упадёт

далее переходим в утилиты 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/1.JPG)

нажимаем edit configuration

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/2.JPG)

не забыть добавить 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/3.JPG)

запускаю тест

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/4.JPG)

далее изменим код, добавив ещё один тест

```python
from solution import division

def test_division_good():
    assert division(10, 2) == 5
def test_division_one_more():
    assert division(10, 5) == 2
```
получили следующий результат:

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/5.JPG)

Но писать каждый раз ф-ю не есть хорошо. Поэтому пишем надо использовать ```@pytest.mark.parametrize``` 

```python
from solution import division
import pytest

@pytest.mark.parametrize("a, b, expected_result",[(10,2,5),
                                                  (20,10,2),
                                                  (30,-3,-10),
                                                  (5,2,2.5)])

def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result
```
получил следующий результат

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/6.JPG)

## спровоцированная ошибка и проверка на срабатывание
добавим следующий код 
```python

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
```
так как делить на 0 нельзя, то тест должен провалится и выдасть ошибку, но благодаря строчке 
```with pytest.raises(ZeroDivisionError):``` мы сможем узнать провалился ли тест без вывода ошибки. Если тест не провалится, то тут как раз произойдёт ошибка

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/7.JPG)

изменю код, чтобы ошибки не было, но из-за строчки ```with pytest.raises(ZeroDivisionError):``` тест провалится из-за того, что как раз нет ошибки деления на 0
```python

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 1)
```

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/8.JPG)

можно поймать на ошибку типов

```python
from solution import division
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

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/img_readMe/9.JPG)

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