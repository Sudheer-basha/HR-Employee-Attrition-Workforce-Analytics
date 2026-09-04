# DAX Measures
```dax
Total Employees = COUNTROWS('hr_employee_data')
Attrition Rate = DIVIDE(CALCULATE(COUNTROWS('hr_employee_data'), 'hr_employee_data'[Attrition] = "Yes"), [Total Employees])
```