### Создание первой модели данных и ее регистрация в административном приложении Django

+ Django отлично подходит для создания управляемых данными сайтов, поскольку включает простые и вместе с тем мощные средства для выполнения запросов к базе данных из программы на языке Python.

проект будет создан в той директории, в которой сейчас находится консоль

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/1.JPG)

С помощью команды: 

**django-admin startproject blog **

или

**django-admin.py  startproject blog **


создайтся директория с  проектом с названием blog 

зайдём в новую созданую диреторию blog.

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

**Метод get_excerpt ** позволяет в списке всех статей выводить текст статьи не целиком, а показывать первые 140 символов.

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/5.JPG)

В этой же директории откройте файл **admin.py **


![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/6.JPG)


Этот  файл ответственен за настройку страницы записей в административном приложении. 
•	Файл **manage.py ** – файл для командной строки (терминала), который позволяет взаимодействовать с проектом с помощью различных методов.
•	Файл **__init__.py ** – файл необходим для того, чтобы Python рассматривал данный каталог как пакет, т.е., как группу модулей. Это пустой файл.
•	Файл **settings.py **– в нем содержатся настройки для текущего проекта.
•	Файл **urls.py ** –описания URL для текущего проекта. «Оглавление» сайта.
•	Файл **wsgi.py  **– файл для настроек текущего проекта. Не изменяется.

 сохраните в **admin.py ** следующий код:

``` python
from django.contrib import admin
from .models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

admin.site.register(Article, ArticleAdmin)
```

Класс **ArticleAdmin ** нужен для того, чтобы, используя декларативный стиль, описать то, каким образом модель **Article ** должна отображаться в административной панели.

В конце файла вызывается функция **admin.site.register() **, которой передаются два параметра: модель статей и класс, описывающий, как модель должна отображаться в административном интерфейсе. Эта функция объявляет, что данная модель должна быть добавлена в административный интерфейс.


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

**'NAME': os.path.join(BASE_DIR, 'Название новой бд.sqlite3') , (blog)**
```sql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_blog.sqlite3') ,
    }
}
```
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

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/14.JPG)

открываем браузер и вводим 

http://127.0.0.1:8000/

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/15.JPG)

http://127.0.0.1:8000/admin/

производим вход в админку( чтобы в неё войти нужно спомнить пароль и логин, который был введён при создании супер пользователя)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/16.JPG)

но на данном этапе у нас не доступна бд **(Articles)** и при открытии или редактировании у нас возникник исключение
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/17.JPG)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/18.JPG)


теперь добавляем бд в проект для это нужно:

+ выйти из консоли с помощью команды ctrl+break в cmd ( в консоли она отображена как ^c но это не верное отображение)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/19.JPG)

добовляем для бд URL, для этого заходим в  urls.py

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/20.JPG)

и добавляем следующий код
```python
from django.contrib import admin
from django.urls import path
from  articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('articles/',views.Article, name='articles'),

]
```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/21.JPG)

В директории articles в файле views.py 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/22.JPG)

```python
from .models import Article
from django.shortcuts import render

def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})
``` 
**.models** точка указывает, что файл находится в этой же директории, что и **Article**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/21_1.JPG)

после этого можно добавить бд созданную в директории articles в главную бд. Для этого выполним команду:
    
**python manage.py makemigrations**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/23.JPG)


после этого нужно связать 2 бд с помощью команды:

**python manage.py migrate**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/24.JPG)

теперь можно сново включать сервер и запускать проект 
**python manage.py runserver**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/14.JPG)


заходим в админку 

http://127.0.0.1:8000/admin/

и добавляем данные в бд

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/25.JPG)

я добавил 3 штуки

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/26.JPG)

+ с помощью программы управления базами данных sqlite3 (например, SQLite Manager), проверим добавились ли данные в бд не посредственно в приложении 

**! бд называть как я назвал нельзя, но так как это учебная бд, то можно и оставить**

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/27.JPG)

Данные сохранились, теперь добавим ещё одну запись с помощью программы SQLite Manager

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/28.JPG)

В директории articles создадим папку templates для просмотра нашей бд не из под админки

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/29.JPG)

```html
<!DOCTYPE html>
<html lang="ru">
   <head>
      <title>сайт бд</title>
      <meta charset="utf-8">
    
    </head>
   <body>
       <div class="header">
            <img src="{{ STATIC_URL }} /static/img/logo.png"  alt="LOGO"/>
</div>
<div class="archive">
{% for post in posts %}
<div class="one-post">
<h2 class="post-title">{{ post.title }}</h2>
<div class="article-info">
<div class="article-author">{{ post.author.username }}</div>
<div class="article-created- date">{{ post.created_date }}</div>
</div>
<p class="article-text">{{ post.get_excerpt }}</p>
</div>
{% endfor %}
</div>

    </body>
</html>


```

У первого тега <div> установлен класс header, а у второго – archive. Это помогает делать верстку понятной, потому что классы играют роль имен для каждого элемента, из названия класса становится понятно, для чего существует текущий элемент, а также помогает отличать нужные блоки друг от друга при установке стилей.
Во внутрь тега div с классом header добавьте изображение (например, логотип проекта). Пример добавления:  
Во внутрь тега div с классом archive добавьте шаблон для отображения одной статьи. Так как у каждой записи есть название, автор, текст и время создания, для каждого поля записи нужно создать определенный элемнт в разметке страницы. Шаблон одного поста будет выглядеть так:
```sql
<div class="one-post">
<h2 class="post-title">{{ post.title }}</h2>
<div class="article-info">
<div class="article-author">{{ post.author.username }}</div>
<div class="article-created-date">{{ post.created_date }}</div>
</div>
<p class="article-text">{{ post.get_excerpt }}</p>
</div>
```
``` sql    
Поле «название» было помещено в тег <h2> c классом post-title, поля «автор» и «время создания» были помещены в один общий тег <div>, потому что в будущем эти два поля будут визуально находится на одной строке. Поле «текст» обрамлено тегом <p>, который означает один абзац текста (p – сокращение от «paragraph»). Ограничение на отображение только части текста статьи введено из-за того, что некоторые посты могут по размерам занимать несколько страниц, что, недопустимо при отображении списка сразу многих экземпляров.
Однако созданная разметка подходит для отображения одной статьи, а не нескольких. Для корректного отображения необходимо добавить цикл, который бы повторялся столько раз, сколько статей передано в контекст шаблона. Для этого существует шаблоный тег {% for item in list %}, практически идентичен циклу for языка Python. Переменная posts, передаваемая в шаблон, выполняет роль массива. 
```
    Для того, чтобы разметка поддерживала отображение сразу многих записей, достаточно добавить строку начала цикла и строку его завершения:
```python
{% for post in posts %}
<div class="one-post">
<h2 class="post-title">{{ post.title }}</h2>
<div class="article-info">
<div class="article-author">{{ post.author.username }}</div>
<div class="article-created- date">{{ post.created_date }}</div>
</div>
<p class="article-text">{{ post.get_excerpt }}</p>
</div>
{% endfor %}
```
Теперь шаблон готов.

теперь пропишем URL адресс для архива

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/30.JPG)

```python
from django.contrib import admin
from django.urls import path
from  articles import views

urlpatterns = [
     path('admin/', admin.site.urls),
	 path('articles/',views.Article, name='articles'),
	 path('archive/',views.archive, name='archive'), # вот так home будет отображатся
	 path('',views.archive, name='archive'), # вот так home будет отображатся
]


```
![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/31.JPG)

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/web_программирование_и_мобильная_разработка/lab3/imagesProject/32.JPG)