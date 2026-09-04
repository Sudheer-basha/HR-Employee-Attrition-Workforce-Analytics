import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_data(num_records=105000):
    np.random.seed(42)
    
    # Generate dates
    start_date = pd.to_datetime('2010-01-01')
    end_date = pd.to_datetime('2026-09-01')
    days_between = (end_date - start_date).days
    random_days = np.random.randint(0, days_between, num_records)
    hire_dates = start_date + pd.to_timedelta(random_days, unit='D')
    
    # Base logic
    age = np.random.randint(22, 60, num_records)
    total_work_experience = np.maximum(age - 22, np.random.randint(0, 10, num_records))
    
    years_since_hire = (end_date - hire_dates).days / 365.25
    years_at_company = np.minimum(total_work_experience, np.round(years_since_hire, 1))
    
    departments = ['Sales', 'Research & Development', 'Human Resources', 'IT', 'Finance']
    dept_prob = [0.3, 0.4, 0.05, 0.15, 0.1]
    department = np.random.choice(departments, num_records, p=dept_prob)
    
    job_roles = {
        'Sales': ['Sales Executive', 'Sales Representative', 'Manager'],
        'Research & Development': ['Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager'],
        'Human Resources': ['Human Resources', 'Manager'],
        'IT': ['Software Engineer', 'Data Scientist', 'IT Support', 'Manager'],
        'Finance': ['Financial Analyst', 'Accountant', 'Manager']
    }
    
    job_role = []
    for d in department:
        roles = job_roles[d]
        job_role.append(np.random.choice(roles))
        
    job_level = np.random.randint(1, 6, num_records)
    
    # Salary based on job level and experience
    base_salary = 40000 + (job_level * 15000) + (total_work_experience * 1000)
    noise = np.random.normal(0, 5000, num_records)
    salary = np.maximum(30000, np.round(base_salary + noise, 0))
    
    def get_salary_band(sal):
        if sal < 50000: return 'Low'
        elif sal < 90000: return 'Medium'
        elif sal < 130000: return 'High'
        else: return 'Very High'
        
    salary_band = [get_salary_band(s) for s in salary]
    
    attrition_prob = np.where((salary_band == 'Low') | (job_level == 1) | (years_at_company < 2), 0.2, 0.05)
    attrition_prob = np.where(np.random.rand(num_records) < 0.1, attrition_prob + 0.1, attrition_prob) # random noise
    
    attrition = np.random.rand(num_records) < attrition_prob
    attrition = ['Yes' if a else 'No' for a in attrition]
    
    exit_dates = []
    for i in range(num_records):
        if attrition[i] == 'Yes':
            days_at_comp = int(years_at_company[i] * 365.25)
            if days_at_comp <= 0: days_at_comp = 10
            exit_date = hire_dates[i] + timedelta(days=np.random.randint(1, days_at_comp + 1))
            if exit_date > end_date: exit_date = end_date
            exit_dates.append(exit_date)
        else:
            exit_dates.append(pd.NaT)
            
    df = pd.DataFrame({
        'Employee_ID': [f'EMP{str(i).zfill(6)}' for i in range(1, num_records + 1)],
        'Employee_Name': [f'Employee_{i}' for i in range(1, num_records + 1)],
        'Gender': np.random.choice(['Male', 'Female', 'Other'], num_records, p=[0.55, 0.43, 0.02]),
        'Age': age,
        'Department': department,
        'Job_Role': job_role,
        'Job_Level': job_level,
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], num_records, p=[0.1, 0.5, 0.3, 0.1]),
        'Years_At_Company': years_at_company,
        'Total_Work_Experience': total_work_experience,
        'Salary': salary,
        'Salary_Band': salary_band,
        'Overtime': np.random.choice(['Yes', 'No'], num_records, p=[0.3, 0.7]),
        'Work_Life_Balance': np.random.randint(1, 5, num_records),
        'Job_Satisfaction': np.random.randint(1, 5, num_records),
        'Environment_Satisfaction': np.random.randint(1, 5, num_records),
        'Performance_Rating': np.random.choice([2, 3, 4], num_records, p=[0.1, 0.7, 0.2]),
        'Training_Hours': np.random.randint(0, 100, num_records),
        'Promotion_Last_Year': np.random.choice([0, 1], num_records, p=[0.8, 0.2]),
        'Manager_Tenure': np.maximum(0, years_at_company - np.random.randint(1, 5, num_records)),
        'Remote_Status': np.random.choice(['On-Site', 'Hybrid', 'Fully Remote'], num_records, p=[0.5, 0.3, 0.2]),
        'Business_Travel': np.random.choice(['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'], num_records, p=[0.1, 0.7, 0.2]),
        'Absence_Days': np.random.randint(0, 30, num_records),
        'Attrition': attrition,
        'Hire_Date': hire_dates,
        'Exit_Date': exit_dates
    })
    
    # Introduce some data quality issues
    num_missing = int(num_records * 0.01)
    df.loc[np.random.choice(df.index, num_missing), 'Age'] = np.nan
    df.loc[np.random.choice(df.index, num_missing), 'Department'] = np.nan
    
    # Save
    out_path = '../data/raw/hr_employee_raw.csv'
    df.to_csv(out_path, index=False)
    print(f"Successfully generated {num_records} records to {out_path}")

if __name__ == '__main__':
    # Make sure cwd is python folder or use relative to file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    generate_data()
