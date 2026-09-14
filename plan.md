# Goals

Admin should be able to download a excel/ a type of doc that will have all the info. 

No need of the pen paper method.

Make this a by user thing as multiple people work the same position at same time but with different Fusion ID's

```
User ID
Name
Shift times (start and end)
Date
Amount of cash earned by the facility (per user and per shift) [Helps compare with the POS report generated for the admin by the POS ] 
```

# User differentiations

1. Admin: downloads teh daily/weekly files and compares with POS given report. Helps debug what went wrong and where.
2. User: Uses software and filles the report, the report is then used by the admin to compare with teh POS report.

# Things to know

## 1. Reports 

### 1.Balance Reports (from the POS)
            1.Admin report: This is the report for all users. Includes **ALL** transactions. 
            2.User report: This report only includes the transactions occurred during a shift for a specific user.
### 2. Shift Reports
            Each user filles out a shift report (currently pen paper) which has opening and closing counts, section where physical cash made during the shift is compared with what Fusion (POS) says what is earned.
### 3. Online and In-person sales [types of sales fusion differentiates into]
            1. Online is the part where all transactions which occurred on the website or any place that is not the actual in person sales. Fusion still clubs it based on who was logged in at that time.
            2. In-person sales is the part where all transactions are recorded when the exchange took place **in front** of the user.

# Database schema ?

```sql
Opening_drawer(
    Name
    Date
    Shift_start_time
    Shift_end_time
    Safe_ID
    B_100
    B_50
    B_20
    B_10
    B_5
    B_1
    C_25
    C_10
    C_05
    C_01
    Total[Calculated by the program] {Preferred be 100$} 
)

Closing_drawer(
    Name
    Date
    Shift_start_time
    Shift_end_time
    Safe_ID
    B_100
    B_50
    B_20
    B_10
    B_5
    B_1
    C_25
    C_10
    C_05
    C_01
    Total[Calculated by the program] {Should not be less than 100$} "What if opening was not a 100$?"
)

Fusion_reports(
    Name
    Date
    Shift_start_time
    Shift_end_time
    Safe_ID
    Fusion_cash [Physical money made by the user according to fusion] {Should match this:{C_Total - O_Total= Fusion_cash}}
    Visa
    Mastercard
    Discover
    Total_CC [Total for Visa,Discover,Mastercard, used to tally later]
)
```
# Tech Stack

## PyPDF
    PDF parsing for fusion daily balance reports.
    If possible should only parse the date, time, user name, location, and totals for the specific transaction sections.

# Flow
 
User Login-> New shift -> Opening drawer -> normal shift stuff -> Closing drawer -> Upload fusion daily balance report -> Balanced/Over/Under 

All shifts being saved and user able to see previous shifts.

# Backend expectations
1.Totals for all the reports 
2. Math behind all the tally marks (Closing total - Opening total == Fusion cash total)
