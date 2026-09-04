import pandas as pd
import os

def segmentation():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    df = pd.read_csv('../data/processed/hr_employee_cleaned.csv')
    
    # Segment by Job Level and Gender
    segmentation = df.groupby(['Job_Level', 'Gender']).size().unstack()
    print("Workforce Segmentation:")
    print(segmentation)

if __name__ == '__main__':
    segmentation()
