let header = document.querySelector('header');
let section = document.querySelector('section');

//let requestURL = 'https://mdn.github.io/learning-area/javascript/oojs/json/superpersonal.json';
//let requestURL = 'json/superpersonal.json';
let requestURL = "http://xn--80aaklnzueid0i.xn--h1ahn.xn--p1acf/json/json.php"; //comanServer.php
let request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'text'; // now we're getting a string!
request.send();

request.onload = function () {
    let fullPersonalText = request.response;// get the string from the response
    let personal = JSON.parse(fullPersonalText); // convert it to an object
    mainInformation(personal);

}





function mainInformation(jsonObj) {


    for (let i = 0; i < jsonObj.length; i++) {

        let personal;
        jsonObj[i].forEach(element => {
            personal = element;
        });

        let myArticle = document.createElement('article');
        myArticle.className = "card";

        let myH2 = document.createElement('h2');
        let myPara1 = document.createElement('p');
        let myPara2 = document.createElement('p');
        let myPara3 = document.createElement('p');
        let myPara4 = document.createElement('p');

        console.log(personal);

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





        // personal.personal_company_car.forEach(element => {
        //     let cars = element;
        //     let carBrand = document.createElement('li');
        //     let model = document.createElement('li');
        //     let dateBild = document.createElement('li');
        //     carBrand.textContent = "Марка автомобиля: " + cars.car_brand;
        //     model.textContent = "Модель авто: " + cars.model;
        //     dateBild.textContent = "Год выпуска авто: " + cars.date_bild;

        //     carList.appendChild(carBrand);
        //     carList.appendChild(model);
        //     carList.appendChild(dateBild);
        // });



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
