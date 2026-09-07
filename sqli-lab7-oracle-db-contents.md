Title: SQL injection attack, listing the database contents on Oracle 

Vulnerability: sqli (sql injection) 

Severity: High 

Attack Surface: SQL injection vulnerability in the product category filter 


What Happened: 

STEPS:

1. Finding the columns by using NULL query and in that only we have to identify which column using text data type.
2. Listing tables by using the below query in oracle query is different You can list tables by querying `all_tables`: `SELECT * FROM all_tables`
3. Listing columns : You can list columns by querying `all_tab_columns`: `SELECT * FROM all_tab_columns WHERE table_name = 'USERS'`
4. Then we have identified the password column and username column from user table and resolved the lab

Payload: ' UNION SELECT USERNAME_WXFVDE, PASSWORD_EJXPGI FROM USERS_HCQQVY-- 

Impact: An attacker can extract all usernames and passwords from the database giving full account takeover of any user including administrators. Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code. What I Learned: I have learned the all_tables from oracle database completly by retriving the information database and tables and columns. And i have learned how to construct the payload for this.

* Counted columns ✅
* Listed schemas ✅
* Found target table ✅
* Extracted column names ✅
* Dumped credentials ✅

Mistakes I Made: i made an lot of spelling mistakes in payload consttruction which leads to internal server error.all_tables-> listing tables all_tab_columns -> listing columns
- Forgot SELECT keyword in UNION query
- Forgot to put table name after FROM clause
