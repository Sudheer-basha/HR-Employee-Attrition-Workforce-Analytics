-- Salary Analysis
SELECT Job_Role, AVG(Salary) as Avg_Salary, MIN(Salary) as Min_Salary, MAX(Salary) as Max_Salary FROM hr_employee_data GROUP BY Job_Role ORDER BY Avg_Salary DESC;