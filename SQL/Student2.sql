create database Student2;
create table Student2.a
(
Roll int PRIMARY KEY,
FirstName varchar(255) ,
email varchar(255) UNIQUE ,
phone int unique ,
trade varchar(255)
);
insert into Student2.a(Roll,FirstName,email,phone,trade)
values(2211009,'Utkarsh','utkarsh@gail.com',8210,'CDE');



