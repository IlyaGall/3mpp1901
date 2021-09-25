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