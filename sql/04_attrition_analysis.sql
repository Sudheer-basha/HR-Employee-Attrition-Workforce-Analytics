-- Attrition Analysis
SELECT Department, SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Attrition_Rate FROM hr_employee_data GROUP BY Department;