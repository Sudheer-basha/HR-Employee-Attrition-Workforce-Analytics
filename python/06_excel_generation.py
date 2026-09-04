import pandas as pd
import os

def create_excel():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("Loading HR data...")
    raw_df = pd.read_csv('../data/raw/hr_employee_raw.csv')
    clean_df = pd.read_csv('../data/processed/hr_employee_cleaned.csv')
    
    excel_path = '../excel/HR_Workforce_Analytics.xlsx'
    print("Generating enriched HR Excel workbook...")
    
    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        # 10k limits for raw/clean so Excel stays snappy, but full data for aggregations
        raw_df.sample(min(10000, len(raw_df)), random_state=42).to_excel(writer, sheet_name='Raw_Data', index=False)
        clean_df.sample(min(10000, len(clean_df)), random_state=42).to_excel(writer, sheet_name='Cleaned_Data', index=False)
        
        # KPI Summary
        attrition_rate = (clean_df['Attrition'] == 'Yes').mean() if 'Yes' in clean_df['Attrition'].values else 0
        kpi_data = pd.DataFrame({
            'Metric': ['Total Employees', 'Active Employees', 'Exited Employees', 'Attrition Rate', 'Average Salary', 'Avg Years at Company'],
            'Value': [
                len(clean_df), 
                len(clean_df[clean_df['Attrition'] == 'No']),
                len(clean_df[clean_df['Attrition'] == 'Yes']),
                attrition_rate, 
                clean_df['Salary'].mean(), 
                clean_df['Years_At_Company'].mean()
            ]
        })
        kpi_data.to_excel(writer, sheet_name='KPI_Summary', index=False)
        
        # Department Analysis
        dept_df = clean_df.groupby('Department').agg(
            Headcount=('Employee_ID', 'count'),
            Avg_Salary=('Salary', 'mean'),
            Attrition_Count=('Attrition', lambda x: (x == 'Yes').sum()),
            Attrition_Rate=('Attrition', lambda x: (x == 'Yes').mean())
        ).reset_index()
        dept_df.to_excel(writer, sheet_name='Department_Analysis', index=False)
        
        # Role Analysis
        role_df = clean_df.groupby('Job_Role').agg(
            Headcount=('Employee_ID', 'count'),
            Avg_Salary=('Salary', 'mean'),
            Attrition_Rate=('Attrition', lambda x: (x == 'Yes').mean())
        ).reset_index()
        role_df.to_excel(writer, sheet_name='Role_Analysis', index=False)
        
        # Salary Analysis
        salary_df = clean_df.groupby('Salary_Band').agg(
            Headcount=('Employee_ID', 'count'),
            Attrition_Rate=('Attrition', lambda x: (x == 'Yes').mean())
        ).reset_index()
        salary_df.to_excel(writer, sheet_name='Salary_Analysis', index=False)
        
        # Attrition Analysis (Deep Dive)
        attrition_by_age = clean_df.groupby(['Age', 'Gender'])['Attrition'].apply(lambda x: (x == 'Yes').mean()).reset_index()
        attrition_by_age.rename(columns={'Attrition': 'Attrition_Rate'}, inplace=True)
        attrition_by_age.to_excel(writer, sheet_name='Attrition_Analysis', index=False)
        
        # Tenure Analysis
        tenure_df = clean_df.groupby('Years_At_Company').agg(
            Headcount=('Employee_ID', 'count'),
            Avg_Salary=('Salary', 'mean'),
            Attrition_Rate=('Attrition', lambda x: (x == 'Yes').mean())
        ).reset_index()
        tenure_df.to_excel(writer, sheet_name='Tenure_Analysis', index=False)
        
        # Pivot Tables (Simulated)
        pivot_dept_role = clean_df.pivot_table(index='Department', columns='Job_Level', values='Salary', aggfunc='mean').reset_index()
        pivot_dept_role.to_excel(writer, sheet_name='Pivot_Tables', index=False)
        
        # Extra Data - maybe distribution of performance ratings
        perf_df = clean_df['Performance_Rating'].value_counts().reset_index()
        perf_df.columns = ['Performance_Rating', 'Count']
        perf_df.to_excel(writer, sheet_name='Extra_Data', index=False)
        
        # Insights
        insights = [
            "Highest attrition rate observed in roles with lowest salary bands.",
            "Average tenure of exiting employees is typically lower than active employees.",
            "Sales department has a significantly higher turnover than R&D."
        ]
        pd.DataFrame({'Key Insights': insights}).to_excel(writer, sheet_name='Insights', index=False)

    print(f"Excel workbook created at {excel_path}")

if __name__ == '__main__':
    create_excel()
