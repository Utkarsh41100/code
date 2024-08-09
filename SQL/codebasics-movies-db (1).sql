-- Create a new database
CREATE DATABASE CompanyDB;
-- Use the newly created database
USE CompanyDB;
-- Create a table for departments
CREATE TABLE Departments (
  department_id INT PRIMARY KEY AUTO_INCREMENT,
  department_name VARCHAR(50) NOT NULL
);
-- Create a table for employees
CREATE TABLE Employees (
  employee_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  department_id INT,
  hire_date DATE,
  salary DECIMAL(10, 2),
  FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
-- Insert data into Departments table
INSERT INTO Departments (department_name)
VALUES ('Sales'),
  ('Marketing'),
  ('HR'),
  ('IT');
-- Insert data into Employees table
INSERT INTO Employees (
    first_name,
    last_name,
    department_id,
    hire_date,
    salary
  )
VALUES ('John', 'Doe', 1, '2020-01-15', 55000.00),
  ('Jane', 'Smith', 2, '2019-03-23', 62000.00),
  ('Emily', 'Johnson', 3, '2018-07-01', 50000.00),
  ('Michael', 'Brown', 4, '2021-06-15', 70000.00);
-- Select all employees
SELECT *
FROM Employees;
-- Select employees along with their department names using JOIN
SELECT e.first_name,
  e.last_name,
  d.department_name,
  e.salary
FROM Employees e
  JOIN Departments d ON e.department_id = d.department_id;
-- Update the salary of an employee
UPDATE Employees
SET salary = 75000.00
WHERE first_name = 'John'
  AND last_name = 'Doe';
-- Delete an employee record
DELETE FROM Employees
WHERE first_name = 'Emily'
  AND last_name = 'Johnson';
-- Drop the Employees table
DROP TABLE Employees;
-- Drop the Departments table
DROP TABLE Departments;
-- Drop the database
DROP DATABASE CompanyDB;