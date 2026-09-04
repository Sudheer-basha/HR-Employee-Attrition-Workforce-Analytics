import pandas as pd
import os

def attrition_analysis():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    df = pd.read_csv('../data/processed/hr_employee_cleaned.csv')
    
    # Attrition by various factors
    print("Attrition by Department:")
    print(df.groupby('Department')['Attrition'].value_counts(normalize=True).unstack() * 100)
    
    print("\nAttrition by Salary Band:")
    print(df.groupby('Salary_Band')['Attrition'].value_counts(normalize=True).unstack() * 100)

if __name__ == '__main__':
    attrition_analysis()
