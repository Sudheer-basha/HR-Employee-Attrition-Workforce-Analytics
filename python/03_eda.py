import pandas as pd
import os

def run_eda():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    df = pd.read_csv('../data/processed/hr_employee_cleaned.csv')
    
    print("Exploratory Data Analysis")
    print("=========================")
    print(f"Total Records: {len(df)}")
    print(f"Attrition Rate: {(df['Attrition'] == 'Yes').mean() * 100:.2f}%")
    print("\nDepartment Distribution:")
    print(df['Department'].value_counts(normalize=True) * 100)
    print("\nAverage Salary by Department:")
    print(df.groupby('Department')['Salary'].mean())

if __name__ == '__main__':
    run_eda()
