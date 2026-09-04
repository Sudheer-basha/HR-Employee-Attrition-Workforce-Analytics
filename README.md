# HR Employee Attrition & Workforce Analytics

A comprehensive data analytics portfolio project analyzing workforce structure, employee attrition, compensation, job satisfaction, tenure, and department-level trends to identify key drivers of employee turnover.

## Business Problem
The organization is facing a rising employee attrition rate, which is increasing recruitment costs and causing knowledge loss. The HR department needs to understand the underlying causes of turnover—whether it's driven by compensation, job satisfaction, work-life balance, or lack of career progression.

## Objective
To build an end-to-end HR analytics pipeline using a dataset of 100,000+ employee records to identify high-risk employee segments and provide data-driven retention strategies using Python, SQL, Excel, and Power BI.

## Dataset
- **Volume:** 100,000+ employee records.
- **Scope:** Includes demographics (Age, Gender), job details (Department, Role, Level, Salary), performance metrics (Rating, Training Hours), and satisfaction survey results.

## Data Dictionary
| Column | Description |
|---|---|
| `Employee_ID` | Unique identifier for the employee |
| `Department` | Department of the employee (e.g., Sales, R&D) |
| `Job_Role` | Specific job title |
| `Salary` / `Salary_Band` | Compensation details |
| `Years_At_Company` | Total tenure at the organization |
| `Job_Satisfaction` | Self-reported satisfaction score (1-4) |
| `Overtime` | Whether the employee works overtime (Yes/No) |
| `Attrition` | Target variable: Did the employee leave? (Yes/No) |

## Tools & Technologies
- **Python:** `pandas`, `numpy` (Data Processing, EDA, Missing Value Imputation)
- **SQL:** Aggregations, CTEs, Window functions to rank attrition by department and salary
- **Excel:** Automated Pivot Tables, KPI Summaries, formatting via `xlsxwriter`
- **Power BI:** Data Modeling, DAX Measures for attrition tracking

## Project Architecture
1. **Data Generation & Quality Check:** Synthetic realistic 100k+ row HR dataset generated and validated.
2. **Data Cleaning (Python):** Handling missing values, standardizing text fields, and validating dates.
3. **Database Analysis (SQL):** Deep-dive SQL queries answering specific workforce questions.
4. **Excel Dashboard:** Programmatically generated multi-sheet workbook with Pivot Tables and KPIs.
5. **BI Integration:** Power BI schema and DAX documentation prepared for dashboarding.

## Key Performance Indicators (KPIs)
- Total Active Employees & Total Exits
- Attrition Rate (%)
- Average Salary & Average Tenure
- Job Satisfaction Score Averages

## Key Insights
1. **Salary Correlation:** Employees in the lowest salary band exhibit an attrition rate nearly double that of higher bands.
2. **Overtime Burnout:** Employees working regular overtime show significantly lower work-life balance scores and higher turnover.
3. **Departmental Risk:** The Sales department has the highest overall turnover, specifically among entry-level Sales Representatives.
4. **Tenure Flight Risk:** The highest risk of attrition occurs around the 2-3 year mark, indicating a lack of mid-level promotion opportunities.

## Business Recommendations
- **Compensation Review:** Conduct a market salary adjustment for entry-level roles in the Sales department to reduce immediate flight risk.
- **Overtime Policy:** Implement strict overtime monitoring and mandate time-in-lieu to improve work-life balance scores.
- **Career Pathways:** Introduce structured promotion pathways and mentorship programs at the 2-year tenure mark to improve mid-level retention.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the python scripts in the `python/` folder sequentially to generate data, clean it, and output the Excel dashboard.
4. Review the SQL scripts in `sql/` and Power BI documentation in `powerbi/`.