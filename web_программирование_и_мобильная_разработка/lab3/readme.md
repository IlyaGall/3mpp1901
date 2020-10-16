### Создание первой модели данных и ее регистрация в административном приложении Django

+ Django отлично подходит для создания управляемых данными сайтов, поскольку включает простые и вместе с тем мощные средства для выполнения запросов к базе данных из программы на языке Python.

проект будет создан в той директории, в которой сейчас находится консоль

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/1.JPG)

С помощью команды: 

**django-admin startproject blog (bold)**

или

**django-admin.py  startproject blog (bold)**


создайётся директория с  проектом с названием blog 

задём в новую созданую диреторию blog.

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/2.JPG)

после этого выполним команду:

**python manage.py startapp articles (blog)**

эта команда создаст новое приложение

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/3.JPG)


Зайдём в директорию articles, а в ней файл models.py сохраните код:

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/4.JPG)

```python
from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __unicode__ (self):
        return "%s: %s" % (self.author.username, self.title)
    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
```

Будущая модель статей будет иметь 4 поля:
+ заголовок,
+ автор, 
+ текст 
+ время создания (в последнем значение будет устанавливаться автоматически).

**Метод get_excerpt (bold)** позволяет в списке всех статей выводить текст статьи не целиком, а показывать первые 140 символов.

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/5.JPG)

В этой же директории откройте файл **admin.py (bold)**


![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/6.JPG)


Этот  файл ответственен за настройку страницы записей в административном приложении. 
•	Файл **manage.py (bold)** – файл для командной строки (терминала), который позволяет взаимодействовать с проектом с помощью различных методов.
•	Файл **__init__.py (bold)** – файл необходим для того, чтобы Python рассматривал данный каталог как пакет, т.е., как группу модулей. Это пустой файл.
•	Файл **settings.py (bold)**– в нем содержатся настройки для текущего проекта.
•	Файл **urls.py (bold)** –описания URL для текущего проекта. «Оглавление» сайта.
•	Файл **wsgi.py  (bold)**– файл для настроек текущего проекта. Не изменяется.

 сохраните в **admin.py (bold)** следующий код:

``` python
from django.contrib import admin
from .models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
admin.site.register(Article, ArticleAdmin)
```

Класс **ArticleAdmin (bold)**нужен для того, чтобы, используя декларативный стиль, описать то, каким образом модель **Article (bold)** должна отображаться в административной панели.

В конце файла вызывается функция **admin.site.register() (bold)**, которой передаются два параметра: модель статей и класс, описывающий, как модель должна отображаться в административном интерфейсе. Эта функция объявляет, что данная модель должна быть добавлена в административный интерфейс.


![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/7.JPG)

перейдём в другую  директорию, в директорию blog blog

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/8.JPG)

заёдём в файл setting.py

добавим в него библиотеку **import os (blog)**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/9.JPG)

Подключить приложение **'articles',  (blog)**  в  файле settings.py

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/10.JPG)

в этом же файле заменить название бд(по желанию)

для этого нужно найти строчку **DATABASES (blog)** в файле  settings.py

и изменить **NAME (blog)**.

**NAME': os.path.join(BASE_DIR, 'Название новой бд.sqlite3') , (blog)**

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_blog.sqlite3') ,
    }
}

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/11.JPG)

Теперь можем мигрировать созданную бд((т.е. создаем бд)

с помощью команды:

**python manage.py migrate (blog)**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/12.JPG)

После этого команды создаём суперпользователя( он нужен для входа на сайт)

**! Нужно будет запомнить логин и пароль который вводишь (blog)**.

с помощью команды:

**python manage.py createsuperuser (blog)**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/13.JPG)


запускаем сервер, чтобы проверить работает ли приложение.

с помощью команды:

**python manage.py runserver (blog)**

открываем браузер и вводим 

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin/


![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/1.JPG)

### display

Определяет flex контейнер; **inline (bold)**  или **block (bold)** в зависимости от заданного значения. Включает flex контекст для всех потомков первого уровня.
```css
.container{
	display: flex; /* or inline-flex */
}
```
Имейте в виду:

Обратите внимание, что CSS-столбцы columns не влияют на flex контейнер.

### flex-direction

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/2.JPG)

Устанавливает основную ось, таким образом определяя направление flex элементов, помещаемых в flex контейнер. Flexbox — это (помимо дополнительной упаковки) концепция однонаправленного макета. Думайте о flex элементах, как о первичных раскладках в горизонтальных рядах или вертикальных столбцах.

```css
.container {
  flex-direction: row | row-reverse | column | column-reverse;
}
```

+ **row (по умолчанию): (bold)** слева направо в ltr; справа налево в rtl
+ **row-reverse: (bold)**  справа налево ltr; слева направо в rtl
+ **column: (bold)** так же, как и row но сверху вниз
+ **column-reverse: (bold)** то же самое, row-reverse но снизу вверх

## flex-wrap

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/3.JPG)


По умолчанию гибкие элементы будут пытаться уместиться на одной строке. Вы можете изменить это и позволить элементам переходить на новую строку по мере необходимости с помощью этого свойства.
```css
.container{
  flex-wrap: nowrap | wrap | wrap-reverse;
}
```
+ **nowrap (по умолчанию): (bold)** все flex элементы будут в одной строке
+ **wrap: (bold)** flex-элементы будут перенесены на несколько строк сверху вниз.
+ **wrap-reverse: (bold)** flex-элементы будут перенесены на несколько строк снизу вверх.

Посмотреть визуальные демоверсии поведения flex-wrap можно здесь.
https://css-tricks.com/almanac/properties/f/flex-wrap/

## flex-flow (Применяется к: родительскому элементу flex-контейнера)

Это сокращение для flex-direction и flex-wrap свойств, которые вместе определяют основные и поперечные оси flex контейнера. Значением по умолчанию является row nowrap.
```css
flex-flow: <‘flex-direction’> || <‘flex-wrap’>
```
### justify-content

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/4.JPG)

Это свойство определяет выравнивание вдоль главной оси. Оно помогает распределить дополнительный остаток свободного пространства, когда-либо все flex элементы в строке негибкие, либо гибкие, но достигли своего максимального размера. Это также обеспечивает некоторый контроль над выравниванием элементов, когда они переполняют линию.
```css
.container {
  justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly | start | end | left | right ... + safe | unsafe;
}
```
+ **flex-start (по умолчанию): (bold)** элементы сдвинуты в начало flex-direction направления.
+ **flex-end: (bold)** элементы сдвинуты ближе к концу flex направления.
+ **start: (bold)**элементы сдвинуты к началу writing-mode направления.
+ **end: (bold)**элементы сдвинуты в конце writing-mode направления.
+ **left: (bold)** элементы сдвинуты по направлению к левому краю контейнера, если это не имеет смысла flex-direction, тогда он ведет себя как start.
+ **right: (bold)** элементы сдвинуты по направлению к правому краю контейнера, если это не имеет смысла flex-direction, тогда он ведет себя как start.
+ **center:  (bold)**элементы центрированы вдоль линии
+ **space-between: (bold)** элементы равномерно распределены по линии; первый элемент находится в начале строки, последний элемент в конце строки
+ **space-around: (bold)** элементы равномерно распределены по линии с одинаковым пространством вокруг них. Обратите внимание, что визуально пространства не равны, так как все элементы имеют одинаковое пространство с обеих сторон. Первый элемент будет иметь одну единицу пространства напротив края контейнера, но две единицы пространства между следующим элементом, потому что у следующего элемента есть свой собственный интервал, который применяется.
+ **space-evenly: (bold)** элементы распределяются таким образом, чтобы расстояние между любыми двумя элементами (и расстояние до краев) было одинаковым.

Обратите внимание, что поддержка браузером этих значений имеет свои нюансы. Например,  **space-between (bold)** никогда не получал поддержку Edge, а start / end / left / right еще нет в Chrome. В MDN есть подробные графики. Самые безопасные значения это **flex-start, flex-end и center. (bold)** flex-start, flex-end и center.

Есть также два дополнительных ключевых слова, которые вы можете связать с этими значениями: **safe(bold)** и **unsafe (bold)**. Использование safe гарантирует, что как бы вы ни занимались этим типом позиционирования, вы не сможете расположить элемент таким образом, чтобы он отображался за пределами экрана (например, сверху) так, чтобы содержимое тоже не могло быть прокручено (это называется «потеря данных»).

## align-items

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/5.JPG)

Это свойство определяет поведение по умолчанию того, как flex элементы располагаются вдоль поперечной оси на текущей линии. Думайте об этом как о justify-content версии для поперечной оси (перпендикулярной главной оси).
```css
.container {
  align-items: stretch | flex-start | flex-end | center | baseline | first baseline | last baseline | start | end | self-start | self-end + ... safe | unsafe;
}
```


**stretch (по умолчанию): (bold)**растягивать, чтобы заполнить контейнер (все еще соблюдаются min-width / max-width)
**flex-start / start / self-start: (bold)**элементы размещаются в начале поперечной оси. Разница между ними невелика и заключается в соблюдении flex-direction правил или writing-mode правил.
**flex-end / end / self-end: (bold)**элементы располагаются в конце поперечной оси. Разница опять-таки тонкая и заключается в соблюдении flex-direction или writing-mode правил.
**center: (bold)**элементы центрированы по поперечной оси
**baseline: (bold)**элементы выровнены, по их базовой линии

**safe (bold)** и **unsafe (bold)**ключевые слова модификаторов могут быть использованы в сочетании со всеми из этих ключевых слов (хотя это поддерживается не всеми браузерами), это помогает предотвратить выравнивание элементов таким образом, что содержание становится недоступным.
## align-content

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/6.JPG)

Это свойство выравнивает линии в пределах flex контейнера, когда есть дополнительное пространство на поперечной оси, подобно тому, как **justify-content (bold)** выравнивает отдельные элементы в пределах главной оси.

Примечание: это свойство не действует, когда есть только одна строка flex элементов.
```css
.container {
  align-content: flex-start | flex-end | center | space-between | space-around | space-evenly | stretch | start | end | baseline | first baseline | last baseline + ... safe | unsafe;
}
```

**flex-start / start: (bold)** элементы, сдвинуты в начало контейнера. Более поддерживаемый flex-start использует, flex-direction в то время как start использует writing-mode направление.
**flex-end / end: (bold)** элементы, сдвинуты в конец контейнера. Более поддерживаемый flex-end использует flex-direction в то время как end использует writing-mode направление.
**center: (bold)** элементы выровнены по центру в контейнере
**space-between: (bold)** элементы равномерно распределены; первая строка находится в начале контейнера, а последняя — в конце
**space-around: (bold)** элементы равномерно распределены с равным пространством вокруг каждой строки
**space-evenly: (bold)** элементы распределены равномерно, вокруг них одинаковое пространство
**stretch (по умолчанию): (bold)** линии растягиваются, чтобы занять оставшееся пространство

**safe (bold)** и **unsafe (bold)** ключевые слова модификаторов могут быть использованы в сочетании со всеми из этих ключевых слов (хотя это поддерживается не всеми браузерами), это помогает предотвратить выравнивание элементов таким образом, что содержание становится недоступным.
## Свойства для первых дочерних элементов(flex элементы)

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/7.JPG)

order

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/7_1.JPG)

По умолчанию flex элементы располагаются в исходном порядке. Однако свойство order управляет порядком их появления в контейнере flex.
```css
.item {
  order: <integer>; /* default is 0 */
}
```

## flex-grow

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/9.JPG)


Это свойство определяет способность flex элемента растягиваться в случае необходимости. Оно принимает значение от нуля, которое служит пропорцией. Это свойство, какое количество доступного пространства внутри гибкого контейнера должен занимать элемент.

Если для всех элементов **flex-grow (bold)** установлено значение 1, оставшееся пространство в контейнере будет равномерно распределено между всеми дочерними элементами. Если один из дочерних элементов имеет значение 2, этот элемент займет в два раза больше места, чем остальные (или попытается, по крайней мере).
```css
.item {
  flex-grow: <number>; /* default 0 */
}
```
Отрицательные числа не поддерживаются.

## flex-shrink

Это свойство определяет способность гибкого элемента сжиматься при необходимости.
```css
.item {
  flex-shrink: <number>; /* default 1 */
}
```

Отрицательные числа не поддерживаются.

## flex-basis

Это свойство определяет размер элемента по умолчанию перед распределением оставшегося пространства. Это может быть длина (например, 20%, 5rem и т.д.) Или ключевое слово. Ключевое слово **auto (bold)** означает «смотри на мое width или height свойство». Ключевое слово **content (bold)**означает «размер на основе содержимого элемента» — это ключевое слово все еще не очень хорошо поддерживается, так что трудно проверить что для него используется **max-content, min-content (bold)** или **fit-content.(bold)**
```css
.item {
  flex-basis: <length> | auto; /* default auto */
}
```

Если установлено значение **0 (bold)**, дополнительное пространство вокруг содержимого не учитывается. Если установлено значение **auto (bold)**, дополнительное пространство распределяется в зависимости от его **flex-grow (bold)** значения.
![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/8_1.JPG)

## flex
Это сокращение для использования **flex-grow, flex-shrink и flex-basis (bold)** вместе. Второй и третий параметры (**flex-shrink и flex-basis (bold)**) являются необязательными. По умолчанию это **0 1 auto (bold)**.
```css
.item {
  flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
}
```

**Рекомендуется использовать это сокращенное свойство (bold)**, а не устанавливать отдельные свойства. Это сокращение разумно устанавливает другие значения.

## align-self
![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/10.JPG)

Это свойство позволяет переопределить выравнивание по умолчанию (или указанное с помощью **align-items (bold)**) для отдельных элементов flex.
Пожалуйста, смотрите **align-items (bold)** свойство, чтобы понять доступные значения.
```css
.item {
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```
Обратите внимание что свойства **float, clear (bold)** и **vertical-align (bold)** не влияют на flex элементы.

## Примеры

Давайте начнем с очень простого примера, решающего почти ежедневную проблему: идеальное центрирование. Самое простое решение для этой задачи — это использовать flexbox.
```css
.parent {
  display: flex;
  height: 300px; /* Или что угодно */
}

.child {
  width: 100px;  /* Или что угодно */
  height: 100px; /* Или что угодно */
  margin: auto;  /* Магия! */
}
```
Так происходит благодаря тому, что свойство вертикального выравнивания margin установленное в **auto (bold)** во flex контейнере, поглощает дополнительное пространство. Таким образом, установка margin в **auto (bold)** сделает объект идеально отцентрированным по обеим осям.

Теперь давайте используем еще несколько свойств. Рассмотрим список из 6 элементов, все с фиксированными размерами, но могут быть и авторазмеры. Мы хотим, чтобы они были равномерно распределены по горизонтальной оси, чтобы при изменении размера браузера все масштабировалось хорошо и без медиа запросов.
```css
.flex-container {
  /* Сначала мы создаем flex контекст */
  display: flex;
  
  /* Затем мы определяем flex-direction и разрешаем элементам переходить на новые строки
   * Запомните, что это то же самое что и:
   * flex-direction: row;
   * flex-wrap: wrap;
   */
  flex-flow: row wrap;
  
  /* Затем мы определяем, как распределяется оставшееся пространство */
  justify-content: space-around;
}
```
Готово. Все остальное — это просто стайлинг.

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/11.JPG)

Если изменить разрешение экрана ли масштаб, то будет так:

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/12.JPG)

Давайте попробуем что-нибудь еще. Представьте, что у нас есть выровненные по правому краю элементы навигации в верхней части нашего веб-сайта, но мы хотим, чтобы они были выровнены по ширине на экранах среднего размера и располагались в один столбец на небольших устройствах. Это достаточно просто.

```css
/* Большие экраны */
.navigation {
  display: flex;
  flex-flow: row wrap;
  /* Это выровняет элементы по конечной части линии на главной оси */
  justify-content: flex-end;
}

/* Средние экраны */
@media all and (max-width: 800px) {
  .navigation {
    /* На экранах среднего размера мы центрируем элементы, равномерно распределяя пустое пространство вокруг элементов */
    justify-content: space-around;
  }
}

/* Маленькие экраны */
@media all and (max-width: 500px) {
  .navigation {
    /* На маленьких экранах мы больше не используем направление строки, а используем столбец */
    flex-direction: column;
  }
}
```

## Большие экраны

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/ext_1.JPG)


## Средние экраны

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/ext_2.JPG)

## Маленькие экраны

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/ext_3.JPG)

Давайте попробуем что-то еще лучше, играя с гибкостью flex элементов! Как насчет 3-колоночного макета в полную высоту страницы с хедором и футером. И не зависит от исходного порядка элементов.

```css
.wrapper {
  display: flex;
  flex-flow: row wrap;
}

/* Мы говорим, что все элементы имеют ширину 100%, через flex-base */
.wrapper > * {
  flex: 1 100%;
}

/* Мы используем исходный порядок для первого мобильно варианта
 * 1. header
 * 2. article
 * 3. aside 1
 * 4. aside 2
 * 5. footer
 */

/* Средние экраны */
@media all and (min-width: 600px) {
  /* Мы говорим обеим боковым панелям встать в одну строку */
  .aside { flex: 1 auto; }
}

/* Большие экраны */
@media all and (min-width: 800px) {
  /* Мы инвертируем порядок первой боковой панели и основной и говорим главному элементу, чтобы он занимал вдвое большую ширину, чем две другие боковые панели
   */
  .main { flex: 2 0px; }
  .aside-1 { order: 1; }
  .main    { order: 2; }
  .aside-2 { order: 3; }
  .footer  { order: 4; }
}
```

## Большие экраны

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/ext_4.JPG)


## Средние экраны

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/ext_5.JPG)

## Маленькие экраны

![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/ext_6.JPG)

## Префикс для Flexbox

Flexbox требует префикса для лучшей поддержки в разных браузерах. Он не только включает в себя предварительные настройки с префиксом вендора, в нем есть совершенно разные имена свойств и значений. Это связано с тем, что спецификации Flexbox со временем менялись, существуют «старые», «tweener» и «новые» версии.

Возможно, лучший способ справиться с этим — написать новый (и последний) синтаксис и запустить свой CSS через Autoprefixer, который очень хорошо справляется с fallback.

Кроме того, вот Sass @mixin, чтобы помочь с некоторыми префиксами, который также дает вам представление о том, что нужно сделать:
```css
@mixin flexbox() {
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}

@mixin flex($values) {
  -webkit-box-flex: $values;
  -moz-box-flex:  $values;
  -webkit-flex:  $values;
  -ms-flex:  $values;
  flex:  $values;
}

@mixin order($val) {
  -webkit-box-ordinal-group: $val;  
  -moz-box-ordinal-group: $val;     
  -ms-flex-order: $val;     
  -webkit-order: $val;  
  order: $val;
}

.wrapper {
  @include flexbox();
}

.item {
  @include flex(1 200px);
  @include order(2);
}
```

### Поддержка в браузерах

Разбита по «версии» flexbox:

+ (new) означает недавний синтаксис из спецификации (например display: flex;)
+ (tweener) означает странный неофициальный синтаксис с 2011 года (например display: flexbox;)
+ (old) означает старый синтаксис с 2009 года (например display: box;)


![Image alt](https://github.com/IlyaGall/html/raw/master/теория/htmlTags_16_FLEXBOX_/imagesTuturial/13.JPG)

lackberry Browser 10+ поддерживает новый синтаксис.

Для получения дополнительной информации о том, как смешивать синтаксисы, чтобы получить лучшую поддержку браузера, пожалуйста, обратитесь к этой статье (CSS-хитрости) или этой статье (DevOpera).

(CSS-хитрости)  https://css-tricks.com/using-flexbox/

 этой статье (DevOpera). https://dev.opera.com/articles/advanced-cross-browser-flexbox/#fallbacks