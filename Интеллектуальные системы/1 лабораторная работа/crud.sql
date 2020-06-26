--различные запросы на INSERT, содержащие данные к таблицам;

select * from db.personal
where personal_salary_assigned >60000;




select db.personal.personal_id, db.personal.personal_name,db.personal.personal_surname ,db.personal.personal_middle_name ,db.personal.personal_dob, 
db.company_car.company_car_model ,db.company_car.company_car_manufacturer ,db.company_car.price ,db.company_car.company_car_id 
from db.personal join  db.company_car
on personal.personal_company_car_id = company_car.company_car_id;




select db.personal.personal_id, db.personal.personal_name,db.personal.personal_surname ,db.personal.personal_middle_name ,db.personal.personal_dob, 
db.company_car.company_car_model ,db.company_car.company_car_manufacturer ,db.company_car.price ,db.company_car.company_car_id 
,db.department.name_departament ,db.department.number_of_people 
from db.personal join  db.company_car
on personal.personal_company_car_id = company_car.company_car_id
join db.department  on db.personal.personal_department_name_id = department.department_id 


select  db.personal.personal_id, db.personal.personal_name,db.personal.personal_surname ,db.personal.personal_middle_name ,db.personal.personal_dob
,db.office.office_number ,db.office.office_number_of_seats ,db.office.office_total_places 
from db.personal join db.office 
on db.personal.personal_office_number_id =db.office .office_id ;

select db.department.department_id, db.department.name_departament,db.department.number_of_people
,db.laboratory.laboratory_name ,db.laboratory.laboratory_budget ,db.laboratory.laboratory_name_cost_of_equipment 
from db.laboratory join db.department 
on db.laboratory.laboratory_id =db.department .department_id ;


select db.personal.personal_id , db.personal.personal_name,db.personal.personal_surname,db.personal.personal_middle_name 
	from db.personal 
where db.personal.personal_office_number_id is null 
	--limit 2 
	for update
	
	
--3 запроса на выборку данных, каждый запрос должен иметь блок WHERE, в котором должны быть связи с как минимумом 2-мя другими таблицами 
--и какие-либо условия фильтрации данных;
	--выведем всесь персонал+ подробную информацию о них, кто имеет служебное авто марки lada 
select db.personal.personal_id, db.personal.personal_name,db.personal.personal_surname ,db.personal.personal_middle_name ,db.personal.personal_dob, 
db.company_car.company_car_model ,db.company_car.company_car_manufacturer ,db.company_car.price ,db.company_car.company_car_id 
,db.department.name_departament ,db.department.number_of_people 
from db.personal join  db.company_car
on personal.personal_company_car_id = company_car.company_car_id
join db.department  on db.personal.personal_department_name_id = department.department_id 
where db.company_car.company_car_manufacturer ='LADA';

---выведем информацию о людях, которые не работают в офисе
select db.personal.personal_id, db.personal.personal_name,db.personal.personal_surname ,db.personal.personal_middle_name ,db.personal.personal_dob, 
db.company_car.company_car_model ,db.company_car.company_car_manufacturer ,db.company_car.price ,db.company_car.company_car_id 
,db.department.name_departament ,db.department.number_of_people 
from db.personal join  db.company_car
on personal.personal_company_car_id = company_car.company_car_id
join db.department  on db.personal.personal_department_name_id = department.department_id 
where db.personal.personal_office_number_id is null ;

---выведем информацию о людях, которые работают в машиностоительнм депертаменте
select db.personal.personal_id, db.personal.personal_name,db.personal.personal_surname ,db.personal.personal_middle_name ,db.personal.personal_dob, 
db.company_car.company_car_model ,db.company_car.company_car_manufacturer ,db.company_car.price ,db.company_car.company_car_id 
,db.department.name_departament ,db.department.number_of_people 
from db.personal join  db.company_car
on personal.personal_company_car_id = company_car.company_car_id
join db.department  on db.personal.personal_department_name_id = department.department_id 
where db.department.name_departament='машиностоительный';

--1 простой запрос на UPDATE к любой таблице по критериям, указанным в блоке WHERE;
--уменьшим з\п всем у кого она выше 60 000
update  db.personal 
set  personal_salary_assigned = 80000
where 	personal_salary_assigned >= 60000;
select * from db.personal ;
--1 сложный запрос на UPDATE -обновление таблицы A в зависимости от данных в таблице B (придумать критерии);
-- повысить з\п кому выданна машина от компании производства фирмы LADA

	
	UPDATE  db.personal 
	set  personal_salary_assigned = personal_salary_assigned+123456 
from db.company_car
	where db.personal.personal_company_car_id =db.company_car.company_car_id 
		and db.company_car.company_car_manufacturer ='LADA';
	select * from db.personal ;


  -- 1 простой запросы на DELETE  - к любой таблице по критериям, указанным в блоке WHERE;

delete from db.personal where personal_surname='Иванов' ;
  
   -- • 1 сложный запрос на DELETE - удаление записей из таблицы A в зависимости от данных в таблице B (придумать критерии);

--удалим сотрудников, которые работают в офисе 2
	delete from db.personal  using db.office 
		where db.personal.personal_office_number_id =db.office.office_id 
		and db.office.office_id =2;
		select * from db.personal ;





