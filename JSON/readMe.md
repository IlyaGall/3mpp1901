## Клиент-серверное приложение JSON 

Логика приложения такая:

+ 1. Сервер каждый раз запоминать данные, которые отправит ему страница. Чтобы убедиться, что данные в порядке, сервер сразу же в ответ будет посылать результат — то, как сервер это запомнил.

+ 2. На клиенте происходит парсер данных, обработка данных и представление их в читаемом виде для пользователя

+ 3. С клиента можно добавить данные, которые сервер должен будет записать в базу данных Json расположенную на сервере 

Состоит из двух частей клиента и сервера.

### сервер

На сервере установлена операционная система ``Apache HTTP-сервер``

Важный момент заключаеться в том, что если сервер заранее всем не сообщит, что он готов работать с запросами, то браузер не даст нашей локальной странице на компьютере получить данные с другого сервера в интернете. Это сделано в целях безопасности, например, чтобы при оплате картой данные не ушли на другой сервер кроме нужного.

Чтобы браузер разрешил нам получать и отправлять данные с сервера, нам нужно настроить сервер. 

Ошибка будет выглядеть так: 

![Image alt](https://github.com/IlyaGall/3mpp1901_ilyaGaluzinskiy/raw/master/JSON/ImgRedme/1.JPG)



Настройка происходит в файле .htaccess: это системный файл, который лежит на сервере и подсказывает серверу, как себя вести в разных ситуациях, интерплетировать можно, как инструкции. Название .htaccess неслучайно: у файла как бы нет имени, но есть расширение .htaccess, и в обычных папках этот файл не будет виден.

Для настройки сервера был создан файл с расширением  ```.htaccess``` . 

прописываем в файл ```.htaccess``` следующие команды:

```htaccess
Header add Access-Control-Allow-Origin "*"
Header add Access-Control-Allow-Headers "origin, x-requested-with, content-type"
Header add Access-Control-Allow-Methods "PUT, GET, POST, DELETE, OPTIONS"
```

+ Первая строка разрешает серверу работать с запросами от любых страниц (хоть это и небезопасно, но это учебный проект поэтому можно). 
+ Вторая строка содержит список разрешённых запросов. 
+ Третья разрешает нужные нам заголовки в запросе.

Фактически этот файл сейчас означает: «разрешаю тебе принимать запросы со всех сайтов, вот такого типа запросы можно принимать, вот такие у них могут быть заголовки». 

```! Файл .htaccess можно не потерять (на некоторых операционках он станет невидимым, как только сохраняешь его как .htaccess — придётся покопаться в настройках, чтобы его раскрыть). ! ```

Дальше идёт настройка php кода, который отвечает за обработку запросов с клиента.


+ 1. Получаем данные от страницы клиента.
+ 2. Проверяем, есть ли на сервере нужный нам файл с данными —  ```data.json```.
+ 3. Если есть — запоминаем его содержимое, а если такого файла нет — создаём его отдельной командой.

1 вариант:

    + Если пустой запрос, то 4 пункт

2 вариант: 
   
    + Всё, что было в этом файле, переводим в массив, с которым умеет работать PHP. Таким способом у нас каждая JSON-запись будет храниться в отдельной ячейке массива.
    + Добавляем новую запись в этот массив — кладём в него то, что пришло со страницы.
    + Записываем это всё обратно в файл и тут же читаем обратно из него — так мы убедимся, что запись прошла нормально и мы можем с этим работать.
+ 4. Отправляем всё содержимое файла(```data.json) на страницу, чтобы там увидеть, что сервер работает как нужно.

```php
<?php
// на какие данные рассчитан этот скрипт
header("Content-Type: application/json");
// 1. Получаем данные от страницы
$data = json_decode(file_get_contents("php://input"));
if (empty($data)) {
    // 2. Проверяем, есть ли на сервере нужный нам файл с данными — json.data.
    // пустой запрос означает, что юзер попросил отпрвить ему данные для посмотра, код аналогичен ниже, за исключением, что ничего не добовляем в json файл
    // Берём новую переменную и пишем в неё имя файла
    $filename = 'data.json';
    // 3. Если есть — запоминаем его содержимое, а если такого файла нет — создаём его отдельной командой.
    if (file_exists($filename)) {
        // Если файл есть — открываем его и читаем данные
        $file = file_get_contents('data.json');
        // Если такого файла нет…
    } else {
    // …то создаём его сами
        $file = fopen("data.json", "a+");
    }
    echo $file;
    unset($file);
    return;
} 
else{

    // 2. Проверяем, есть ли на сервере нужный нам файл с данными — json.data.
    // Берём новую переменную и пишем в неё имя файла
    $filename = 'data.json';
    // 3. Если есть — запоминаем его содержимое, а если такого файла нет — создаём его отдельной командой.
    if (file_exists($filename)) {
        // Если файл есть — открываем его и читаем данные
        $file = file_get_contents('data.json');
        // Если такого файла нет…
    } else {
    // …то создаём его сами
        $file = fopen("data.json", "a+");
    }
    // 4/ Всё, что было в этом файле, переводим в массив, с которым умеет работать PHP. Таким способом у нас каждая JSON-запись будет храниться в отдельной ячейке массива.
    $taskList = json_decode($file, true);
    // 5. Добавляем новую запись в этот массив — кладём в него то, что пришло со страницы.
    $taskList[] = array($data);
    // 6. Записываем это всё обратно в файл и тут же читаем обратно из него — так мы убедимся, что запись прошла нормально и мы можем с этим работать.
    // Записываем данные в файл…
    file_put_contents('data.json', json_encode($taskList, JSON_UNESCAPED_UNICODE)); //JSON_UNESCAPED_UNICODE без него великий и могучий превращаеться в цифры

    // …и сразу считываем их обратно
    $file = file_get_contents('data.json'); // Открыть файл data.json
    // 7. Отправляем всё содержимое файла на страницу, чтобы там увидеть, что сервер работает как нужно.
    echo $file;
    // Освобождаем память от переменных, которые нам пока не нужны
    unset($file);
    unset($taskList);
}
```

Так же есть простой html файл, который отвечает за загрузку базы данных json на локальное хранилище пользователя важно отметить, что тег ``a href="path file json on server"`` указывает на точное место хранения json файла. Для каждого сервера этот путь уникален

вот его код, который отвечает за загрузку:

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>
        Отправляем JSON-данные на сервер
    </title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</head>

<a href="http://xn--80aaklnzueid0i.xn--h1ahn.xn--p1acf/json/data.json" download>Скачать Json файл</a>

</html>
```

### Клиент
разбит на две папки 
+ 1 ```requestJson``` отвечает за пустой запрос, который расчитывает получить базу данных без добовления в неё данных со стороны клиента
+ 2 ```addNewPerson``` отвечает за добовления новых данных в базу данных

#### requestJson


+ ```css``` 
    + ```style.css```
+ ```js```
    + ```jsonScriptver2.js```
+ файла ```requestJson.html```

файл style.css - это Cascading Style Sheets (каскадные таблицы стилей)

```css
.flex-cards {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
.card {
    max-width: 500px; /*максимальный размер */
    width: 100%; /* размер */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Параметры тени */
    margin: 10px;  /* отступы внешние */
    padding: 10px; /* отступы внутриние */
}
.add-data { /* кнопка */
    margin: 10px;
    width: 300px;
    height: 300px;
    cursor: pointer;
    font-size: 30px;
}
.link {
    width: 300px;
}

```

```requestJson.html```
в секцию 
```
<section class="flex-cards">
</section>
```
будут динамически загружаться данные пришедшие со стороны сервера


```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</head>

<header>
</header>

<section class="flex-cards">
</section>

<a class="link" href="../addNewPerson/addNewPerson.html">
    <button class="add-data">добавить данные</button>
</a>

<a class="link" href="http://xn--80aaklnzueid0i.xn--h1ahn.xn--p1acf/donwloadJson.html" download>
    <button class="add-data">скачать БД</button>
</a>

<body>

</body>
<script src="js/jsonScriptver2.js"></script>

</html>
```



```js
let section = document.querySelector('section'); // находим селектор в который будем добовлять данные

let requestURL = "http://xn--80aaklnzueid0i.xn--h1ahn.xn--p1acf/json/json.php"; // адресс сервера на который будут отправленны данные
let request = new XMLHttpRequest();  // создаём новый экземпляр запроса XHR

request.open('GET', requestURL);  // открываем соединение
request.responseType = 'text'; // теперь получаем строку!
request.send();

request.onload = function () {
    let fullPersonalText = request.response;// получить строку из ответа
    let personal = JSON.parse(fullPersonalText); // преобразовать его в объект
    mainInformation(personal);
}

function mainInformation(jsonObj) {
    for (let i = 0; i < jsonObj.length; i++) { // перебор значений
        let personal; // создаем переменную в которую будут загруженны данные с сервера
        jsonObj[i].forEach(element => {
            personal = element;
        });

        let myArticle = document.createElement('article'); // создание элемента
        myArticle.className = "card"; // присвоение класса элементу

        let myH2 = document.createElement('h2');
        let myPara1 = document.createElement('p');
        let myPara2 = document.createElement('p');
        let myPara3 = document.createElement('p');
        let myPara4 = document.createElement('p');

        myPara1.textContent = 'Имя: ' + personal.personal_name;
        myPara2.textContent = 'Фамилия: ' + personal.lastname;
        myPara3.textContent = 'Отчество: ' + personal.middleName;
        myPara4.textContent = 'Дата рождения:' + personal.dob;

        //////////////////
        let myPara5 = document.createElement('p');
        let myPara6 = document.createElement('p');
        let myPara7 = document.createElement('p');
        let myPara8 = document.createElement('p');


        myPara5.textContent = 'Улица: ' + personal.adress_person.country;
        myPara6.textContent = 'город: ' + personal.adress_person.city;
        myPara7.textContent = 'Индекс: ' + personal.adress_person.street;
        myPara8.textContent = 'Страна проживания: ' + personal.adress_person.index;

        /////////////
        let myParaPhone = document.createElement('p');
        myParaPhone.textContent = 'Телефон для связи: ';

        let myList = document.createElement('ul');
        for (let phone = 0; phone < personal.phone.length; phone++) {
            let listItem = document.createElement('li');
            listItem.textContent = personal.phone[phone].type + ' ' + personal.phone[phone].number;
            myList.appendChild(listItem);
        }

        ////////////
        let myPara9 = document.createElement('p');
        let myPara10 = document.createElement('p');
        let myPara11 = document.createElement('p');


        myPara9.textContent = "Номер оффиса " + personal.personal_office_number.number_office;
        myPara10.textContent = "Отдел " + personal.personal_office_number.name_office;
        myPara11.textContent = "Должность " + personal.personal_office_number.position_id;
        //////////////
        let myPara12 = document.createElement('p');
        myPara12.textContent = "Зарплата " + personal.personal_office_number.salary_assigned;
        //////////////
        let myPara13 = document.createElement('p');
        let carList = document.createElement('ul');
        if (personal.personal_company_car[0].car_brand == "" ||
            personal.personal_company_car[0].model == "" ||
            personal.personal_company_car[0].date_bild == "") {
            myPara13.textContent = "Машины: отсутсвует";

        } else {
            myPara13.textContent = "Машины: " + personal.personal_company_car.length;
            for (let car = 0; car < personal.personal_company_car.length; car++) {
                let carBrand = document.createElement('li');
                let model = document.createElement('li');
                let dateBild = document.createElement('li');
                carBrand.textContent = "Марка автомобиля: " + personal.personal_company_car[car].car_brand;
                model.textContent = "Модель:  " + personal.personal_company_car[car].model;
                dateBild.textContent = "Год выпуска: " + personal.personal_company_car[car].date_bild;
                carList.appendChild(carBrand);
                carList.appendChild(model);
                carList.appendChild(dateBild);
            }
        }

        myArticle.appendChild(myH2);
        myArticle.appendChild(myPara1);
        myArticle.appendChild(myPara2);
        myArticle.appendChild(myPara3);
        myArticle.appendChild(myPara4);

        myArticle.appendChild(myPara5);
        myArticle.appendChild(myPara6);
        myArticle.appendChild(myPara7);
        myArticle.appendChild(myPara8);
        myArticle.appendChild(myParaPhone);

        myArticle.appendChild(myList);

        myArticle.appendChild(myPara9);
        myArticle.appendChild(myPara10);
        myArticle.appendChild(myPara11);

        myArticle.appendChild(myPara12);

        myArticle.appendChild(myPara13);
        myArticle.appendChild(carList);

        section.appendChild(myArticle);
    }
}

```