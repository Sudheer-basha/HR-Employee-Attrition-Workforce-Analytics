-- Workforce Analysis
SELECT Department, COUNT(*) as Headcount, AVG(Age) as Avg_Age FROM hr_employee_data GROUP BY Department;