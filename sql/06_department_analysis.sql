-- Department Analysis
SELECT Department, Job_Role, COUNT(*) as Employees FROM hr_employee_data GROUP BY Department, Job_Role ORDER BY Department, Employees DESC;