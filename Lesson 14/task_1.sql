-- Создание таблицы

CREATE TABLE Employees (
    Name TEXT,
    Position TEXT,
    Department TEXT,
    Salary REAL
);

-- Вставка записей

INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('Alice Johnson', 'Manager', 'Sales', 6500),
('Bob Smith', 'Developer', 'IT', 4800),
('Carol White', 'Designer', 'Marketing', 5200),
('David Brown', 'Salesperson', 'Sales', 4000),
('Eva Green', 'HR Specialist', 'HR', 4500);

-- Обновление данных(повышение должности)

UPDATE Employees
SET Position = 'Senior Developer', Salary = 5500
WHERE Name = 'Bob Smith';

-- Добавление нового поля HireDate

ALTER TABLE Employees
ADD COLUMN HireDate DATE;

-- Заполнение дат приема на работу

UPDATE Employees SET HireDate = '2020-03-15' WHERE Name = 'Alice Johnson';
UPDATE Employees SET HireDate = '2021-06-01' WHERE Name = 'Bob Smith';
UPDATE Employees SET HireDate = '2019-11-20' WHERE Name = 'Carol White';
UPDATE Employees SET HireDate = '2022-01-10' WHERE Name = 'David Brown';
UPDATE Employees SET HireDate = '2023-05-05' WHERE Name = 'Eva Green';

-- 6–9. Хранимая функция (на примере PostgreSQL)

CREATE OR REPLACE FUNCTION employee_queries()
RETURNS TABLE (
    ManagerName TEXT,
    HighSalaryName TEXT,
    SalesDeptName TEXT,
    AvgSalary REAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        (SELECT Name FROM Employees WHERE Position = 'Manager' LIMIT 1),
        (SELECT Name FROM Employees WHERE Salary > 5000 LIMIT 1),
        (SELECT Name FROM Employees WHERE Department = 'Sales' LIMIT 1),
        (SELECT AVG(Salary) FROM Employees);
END;
$$ LANGUAGE plpgsql;

SELECT * FROM employee_queries();

-- Удаление таблицы

DROP TABLE Employees;

