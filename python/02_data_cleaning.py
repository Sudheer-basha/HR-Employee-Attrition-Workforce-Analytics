import pandas as pd
import os

def clean_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    df = pd.read_csv('../data/raw/hr_employee_raw.csv')
    
    # Generate data quality report before cleaning
    dq_report = pd.DataFrame({
        'Column': df.columns,
        'Missing_Values': df.isnull().sum().values,
        'Missing_Percentage': (df.isnull().sum().values / len(df)) * 100,
        'Unique_Values': df.nunique().values,
        'Data_Type': df.dtypes.values
    })
    dq_report.to_csv('../reports/data_quality_report.csv', index=False)
    
    # Impute missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Department'] = df['Department'].fillna('Unknown')
    
    # Remove duplicates if any
    df = df.drop_duplicates()
    
    # Ensure correct data types
    df['Hire_Date'] = pd.to_datetime(df['Hire_Date'])
    df['Exit_Date'] = pd.to_datetime(df['Exit_Date'])
    
    # Save cleaned data
    df.to_csv('../data/processed/hr_employee_cleaned.csv', index=False)
    print("Data cleaning completed. Saved processed data and data quality report.")

if __name__ == '__main__':
    clean_data()
