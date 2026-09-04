-- Data Quality Checks
SELECT COUNT(*) AS total_missing_age FROM hr_employee_data WHERE Age IS NULL;
SELECT COUNT(*) AS duplicate_records FROM (SELECT Employee_ID, COUNT(*) FROM hr_employee_data GROUP BY Employee_ID HAVING COUNT(*) > 1) AS sub;