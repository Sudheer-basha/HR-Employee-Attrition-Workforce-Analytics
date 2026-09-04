import pandas as pd
import os

def check_data_quality():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    df = pd.read_csv('../data/raw/hr_employee_raw.csv')
    print("Data Quality Report - Quick Check")
    print("="*40)
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())

if __name__ == '__main__':
    check_data_quality()
