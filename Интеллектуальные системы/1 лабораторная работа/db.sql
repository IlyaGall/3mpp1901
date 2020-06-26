CREATE DATABASE db;
 \connect db
CREATE SCHEMA db;


-- Drop table
-- DROP TABLE db.office;
--офис в котором работают сотрудники
CREATE TABLE db.office (
	 office_id serial primary key--id
	,office_number integer NOT null-- номер офиса в котором работает сотрудник
	,office_number_of_seats integer NOT null-- количество колличество мест
	,office_total_places int NOT null--всего мест в офисе
);



-- Drop table
-- DROP TABLE db.laboratory;
-- лаборатория, если есть
CREATE TABLE db.laboratory (
	laboratory_id serial primary key--id
	,laboratory_name varchar(50) not Null--название лаборатории
	,laboratory_name_cost_of_equipment int--стоимость оборудования
	,laboratory_budget int NOT null --бюджет лаборатории
);

-- Drop table
-- DROP TABLE db.laboratories_costs;
-- затраты лаборатории
CREATE TABLE db.laboratories_costs (
	laboratories_costs_id serial primary key--id
	,id_laboratory int references db.laboratory(laboratory_id)--id проводивший исследования лаборатории
	,laboratories_costs_research_cost int --затраченные средства на проведения исследования
	,laboratories_costs_data_research date NOT null--дата проведения исследования
	,laboratories_costs_spent_time_in_hours int4 NOT null--время затраченное на иследование
);

-- Drop table
-- DROP TABLE db.department;
--отдел в котором работают сотрудники
CREATE TABLE db.department (
	 department_id serial primary key--id
	,name_departament varchar(50) NOT null--название отдела
	,number_of_people varchar(50) --количество людей в отделе
	,availability_of_laboratory_id int references db.laboratory(laboratory_id) --id лаборатории в отделе
);

-- Drop table
-- DROP TABLE db.employee_position;
-- должность сотрудника
CREATE TABLE db.employee_position (
	 employee_position_id serial primary key--id
	,employee_position_job_title varchar(50) NOT null--название должности
	,employee_position_salary_default int NOT null-- з\п по умолчанию
);

-- Drop table
-- DROP TABLE db.company_car;
-- служебное авто
CREATE TABLE db.company_car (
	 company_car_id serial primary key--id
	,company_car_model varchar(50) null --модель машины
	,company_car_manufacturer varchar not null --изготовитель машины
	,price int NOT null--цена автомобиля
);

-- Drop table
-- DROP TABLE db.personal;
--
CREATE TABLE db.personal (
	 personal_id serial primary key--id
	,personal_surname varchar(50) NOT null--фамилия сотрудника
	,personal_name varchar(30) NOT null-- имя сотрудника
	,personal_middle_name varchar(40) --отчество сотрудника
	,personal_dob date NOT null--дата роджения сотрудника 
	,personal_office_number_id integer references db.office(office_id ) -- id офиса сотрудника
	,personal_department_name_id int references db.department(department_id ) NOT null--id отдела сотрудника
	,personal_position_id int references db.employee_position(employee_position_id) NOT null--должность сотрудника
	,personal_salary_assigned integer NOT null-- з\п которуб назначали сотруднику
	,personal_company_car_id integer references db.company_car(company_car_id ) -- id машины
);

insert into db.office(
 office_number							--номер офиса в котором работает сотрудник
,office_number_of_seats 				--колличество мест
,office_total_places					--всего мест в офисе
)values
(1,20,55),
(44,210,1055);

insert into db.laboratory(
	 laboratory_name 					--название лаборатории
	,laboratory_name_cost_of_equipment  --стоимость оборудования
	,laboratory_budget  				--бюджет лаборатории
)values
('web',100000,10000000),('строительная',12345,54321);


insert into db.laboratories_costs (
	 id_laboratory 							--id проводивший исследования лаборатории
	,laboratories_costs_research_cost   	--затраченные средства на проведения исследования
	,laboratories_costs_data_research   	--дата проведения исследования
	,laboratories_costs_spent_time_in_hours --время затраченное на иследование
)values
(2,90, '2013-06-01',100),(1,10, '2019-07-11',133);


insert into db.department (
	 name_departament 						--название отдела
	,number_of_people				 		--количество людей в отделе
	,availability_of_laboratory_id   		--id лаборатории в отделе
)values('исследовательский в области медицины',10,2),
('машиностоительный',15,Null);

insert into db.employee_position (
	 employee_position_job_title 			--название должности
	,employee_position_salary_default 		-- з\п по умолчанию
)values('младший научный сотрудник',1000),('директор',5789);

insert into db.company_car (
	 company_car_model 						--модель машины
	,company_car_manufacturer  				--изготовитель машины
	,price									--цена автомобиля
)values('Niva 4x4 21214','LADA' ,600000),('x5','BNW' ,2500000),('Q6','AUDI' ,1000);

insert into db.personal (
	 personal_surname 							--фамилия сотрудника
	,personal_name 								--имя сотрудника
	,personal_middle_name 						--отчество сотрудника
	,personal_dob 								--дата роджения сотрудника 
	,personal_office_number_id 				    --id офиса сотрудника
	,personal_department_name_id 				--id отдела сотрудника
	,personal_position_id 						--id должность сотрудника
	,personal_salary_assigned 					--з\п которуб назначали сотруднику
	,personal_company_car_id 				    --id машины
)values('Иванов','Иван','Иванович','1977-01-12',null,2,2,1000000,2),
	   ('Петоров','Пётр','Петрович','1970-03-08',2,2,1,10000,1);

--различные запросы на INSERT, содержащие данные к таблицам;









