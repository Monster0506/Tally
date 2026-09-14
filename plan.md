# Tally

A software that takes in a daily balance report pdf from user and counts for opening and closing drawers. 

Compares the opening and closing drawers counts and tallies them with teh amounts from report. Tells user how over/under the drawer is.

# Goals

Admin should be able to download a excel/ a type of doc that will have all the info. 

No need of the pen paper method

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