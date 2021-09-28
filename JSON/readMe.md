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

```requestJson.html: ```

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

```jsonScriptver2.js```:

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

#### addNewPerson



+ ```css``` 
    + ```style.css```
+ ```js```
    + ```jsonServer.js```
+ файла ```addNewPerson.html```

jsonServer.js:

```js
let res;
let newData;
let sendData;
// эта функция сработает при нажатии на кнопку

function addFieldPhone() {
    let type = document.createElement('input')
    type.type = 'text';
    type.className = 'number-phone';
    type.placeholder = 'Тип телефона'
    let numberPhone = document.createElement('input')
    numberPhone.type = 'text';

    numberPhone.className = 'type-phone';
    numberPhone.placeholder = 'номер'
    let addInput = document.querySelector('.type-phones');
    addInput.append(type);
    addInput.append(numberPhone);
}
function fieldNull(nameFieldIsNull) {

    let divAttention = document.querySelector('.attation');
    let attention = document.querySelector('.attation__text');

    attention.textContent = `вниминие поле  "${nameFieldIsNull}" не заполнено, без заполнения этого поля продолжить нельзя`;
    divAttention.classList.add('active')
    setTimeout(function () {
        divAttention.classList.remove('active')

    }, 2000);
}
function addCar() {

    let carBrand = document.createElement('input')
    carBrand.type = 'text';
    carBrand.className = 'car-brand';
    carBrand.placeholder = 'марка'

    let model = document.createElement('input')
    model.type = 'text';
    model.className = 'model';
    model.placeholder = 'модель'

    let dateBild = document.createElement('input')
    dateBild.type = 'text';
    dateBild.className = 'date-bild';
    dateBild.placeholder = 'год выпуска'

    let addInput = document.querySelector('.cars');
    addInput.append(carBrand);
    addInput.append(model);
    addInput.append(dateBild);
}
function sendJSON() {
    // с помощью jQuery обращаемся к элементам на странице по их именам

    let name = document.querySelector('#name');
    if (name.value == "") {
        fieldNull('Имя')
        return;
    }
    let lastname = document.querySelector('#lastname');
    if (lastname.value == "") {
        fieldNull('Фамилия')
        return;
    }
    let middleName = document.querySelector('#middle_name');
    if (middleName.value == "") {
        middleName.textContent = null;
    }
    let dataBD = document.querySelector('#data_bd');
    if (dataBD.value == "") {
        fieldNull('Дата рождения')
        return;
    }
    ////
    let country = document.querySelector('#country');
    if (country.value == "") {
        fieldNull('Страна')
        return;
    }
    let city = document.querySelector('#city');
    if (city.value == "") {
        fieldNull('Город')
        return;
    }
    let street = document.querySelector('#street');
    if (street.value == "") {
        fieldNull('Улица')
        return;
    }
    let index = document.querySelector('#index');
    if (index.value == "") {
        index.textContent = null;
    }
    let adress_person = {
        'country': country.value,
        'city': city.value,
        'street': street.value,
        'index': index.value,
    }
    //////////
    let typePhones = document.querySelectorAll('.type-phone')
    let numberPhones = document.querySelectorAll('.number-phone')
    if (typePhones.value == "") {
        typePhones.textContent = null;
    }

    if (numberPhones[0].value == "") {
        fieldNull('Телефон не указан')
        return;
    }
    let phone = [{
        'type': typePhones[0].value,
        'number': numberPhones[0].value
    }];
    for (let userPhone = 1; userPhone < typePhones.length; userPhone++) {
        phone.push({ 'type': typePhones[userPhone].value, 'number': numberPhones[userPhone].value });
    }
    ////////
    let number = document.querySelector('#id_office');
    if (number.value == "") {
        number.textContent = null;
    }
    let nameOffice = document.querySelector('#name_office');
    if (nameOffice.value == "") {
        nameOffice.textContent = null;
    }
    let position = document.querySelector('#personal_position_id');
    if (position.value == "") {
        fieldNull('Должность')
        return;
    }
    let salaryAssigned = document.querySelector('#personal_salary_assigned');
    if (salaryAssigned.value == "") {
        fieldNull('З\п')
        return;
    }
    let personal_office_number = {
        'number_office': number.value,
        'name_office': nameOffice.value,
        'position_id': position.value,
        'salary_assigned': salaryAssigned.value

    }

    ///
    let carBrand = document.querySelectorAll('.car-brand');
    let model = document.querySelectorAll('.model');
    let dateBild = document.querySelectorAll('.date-bild');
    let personal_company_car = [{
        'car_brand': carBrand[0].value,
        'model': model[0].value,
        'date_bild': dateBild[0].value
    }];
    for (let car = 1; car < carBrand.length; car++) {
        personal_company_car.push({
            'car_brand': carBrand[car].value,
            'model': model[car].value,
            'date_bild': dateBild[car].value
        });


    }


    // а вот сюда мы поместим ответ от сервера
    let result = document.querySelector('.result');
    // создаём новый экземпляр запроса XHR
    let xhr = new XMLHttpRequest();
    // адрес, куда мы отправим нашу JSON-строку
    let url = 'http://xn--80aaklnzueid0i.xn--h1ahn.xn--p1acf/json/json.php'; //comanServer.php
    // открываем соединение
    xhr.open('POST', url, true);
    // устанавливаем заголовок — выбираем тип контента, который отправится на сервер, в нашем случае мы явно пишем, что это JSON
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // когда придёт ответ на наше обращение к серверу, мы его обработаем здесь
    xhr.onreadystatechange = function () {
        // если запрос принят и сервер ответил, что всё в порядке
        if (xhr.readyState === 4 && xhr.status === 200) {
            // запоминаем данные, которые пришли с сервера
            res = this.responseText;
            // выводим то, что ответил нам сервер — так мы убедимся, что данные он получил правильно
            result.innerHTML = this.responseText;
        }
    };
    // преобразуем наши данные в JSON-строку
    data = JSON.stringify({ 'personal_name': name.value, 'lastname': lastname.value, 'middleName': middleName.value, 'dob': dataBD.value, adress_person, phone, personal_office_number, personal_company_car });
    // когда всё готово, отправляем JSON на сервер
    console.log(data)
    xhr.send(data);
}
function editJSON() {
    // переводим данные от сервера в массив, понятный для JavaScript
    console.log(res)
    newData = JSON.parse(res).map(Object.values);
    // добавляем к каждому имени число с его длиной в скобках
    for (let i = newData.length - 1; i >= 0; i--) {
        newData[i][0].name = newData[i][0].name + '(' + newData[i][0].name.length + ')';
        console.log(newData[i][0].name);
    }
    // а вот сюда мы поместим ответ от сервера
    let result = document.querySelector('.result');
    // создаём новый экземпляр запроса XHR
    let xhr = new XMLHttpRequest();
    // адрес, куда мы отправим нашу JSON-строку
    let url = 'http://xn--80aaklnzueid0i.xn--h1ahn.xn--p1acf/json/json.php'; //comanServer.php
    // открываем соединение
    xhr.open('POST', url, true);
    // устанавливаем заголовок — выбираем тип контента, который отправится на сервер, в нашем случае мы явно пишем, что это JSON
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // когда придёт ответ на наше обращение к серверу, мы его обработаем здесь
    xhr.onreadystatechange = function () {
        // если запрос принят и сервер ответил, что всё в порядке
        if (xhr.readyState === 4 && xhr.status === 200) {
            // выводим то, что ответил нам сервер, — так мы убедимся, что данные он получил правильно
            result.innerHTML = this.responseText;
        }
    };
    // преобразуем наши новые данные JSON в строку
    sendData = JSON.stringify(newData);
    // когда всё готово, отправляем JSON на сервер
    xhr.send(sendData);
}
```






