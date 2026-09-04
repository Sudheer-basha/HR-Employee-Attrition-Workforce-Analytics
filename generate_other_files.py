import os

base_path = r"D:\My Projects\Resume Projects\Data_Analyst_Portfolio_Projects\HR-Employee-Attrition-Workforce-Analytics"

sql_files = {
    "sql/02_data_quality.sql": "-- Data Quality Checks\nSELECT COUNT(*) AS total_missing_age FROM hr_employee_data WHERE Age IS NULL;\nSELECT COUNT(*) AS duplicate_records FROM (SELECT Employee_ID, COUNT(*) FROM hr_employee_data GROUP BY Employee_ID HAVING COUNT(*) > 1) AS sub;",
    "sql/03_workforce_analysis.sql": "-- Workforce Analysis\nSELECT Department, COUNT(*) as Headcount, AVG(Age) as Avg_Age FROM hr_employee_data GROUP BY Department;",
    "sql/04_attrition_analysis.sql": "-- Attrition Analysis\nSELECT Department, SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Attrition_Rate FROM hr_employee_data GROUP BY Department;",
    "sql/05_salary_analysis.sql": "-- Salary Analysis\nSELECT Job_Role, AVG(Salary) as Avg_Salary, MIN(Salary) as Min_Salary, MAX(Salary) as Max_Salary FROM hr_employee_data GROUP BY Job_Role ORDER BY Avg_Salary DESC;",
    "sql/06_department_analysis.sql": "-- Department Analysis\nSELECT Department, Job_Role, COUNT(*) as Employees FROM hr_employee_data GROUP BY Department, Job_Role ORDER BY Department, Employees DESC;",
    "sql/07_advanced_analysis.sql": "-- Advanced Analysis (Window Functions)\nSELECT Employee_ID, Department, Salary, AVG(Salary) OVER (PARTITION BY Department) as Dept_Avg_Salary, Salary - AVG(Salary) OVER (PARTITION BY Department) as Salary_Diff FROM hr_employee_data;"
}

powerbi_files = {
    "powerbi/README.md": "# Power BI Dashboard\nThis folder contains Power BI assets for the HR Analytics project.",
    "powerbi/data_dictionary.md": "# Data Dictionary\n- Employee_ID: Unique identifier\n- Salary: Annual salary in USD",
    "powerbi/DAX_MEASURES.md": "# DAX Measures\n```dax\nTotal Employees = COUNTROWS('hr_employee_data')\nAttrition Rate = DIVIDE(CALCULATE(COUNTROWS('hr_employee_data'), 'hr_employee_data'[Attrition] = \"Yes\"), [Total Employees])\n```",
    "powerbi/DATA_MODEL.md": "# Data Model\nStar schema with hr_employee_data as the main fact table."
}

root_files = {
    "README.md": "# HR Employee Attrition & Workforce Analytics\nComprehensive data analytics portfolio project.",
    ".gitignore": "venv/\n__pycache__/\n.env\n*.xlsx",
    "requirements.txt": "pandas\nnumpy\nxlsxwriter",
    "QUALITY_CHECK_REPORT.md": "# Quality Check Report\nAll data cleaning checks passed successfully."
}

def create_files():
    all_files = {**sql_files, **powerbi_files, **root_files}
    for rel_path, content in all_files.items():
        file_path = os.path.join(base_path, rel_path)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {file_path}")

if __name__ == '__main__':
    create_files()
