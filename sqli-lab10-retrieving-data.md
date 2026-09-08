Title : SQL injection UNION attack, retrieving data from other tables 

Vulnerability: SQL injection 

Severity: High 

Attack Surface: SQL injection vulnerability in the product category filter 

What Happened: SQL injection vulnerability in the product category filter and in this we have to identify of the administrator password from the table of users. 
step 1: identifying the columns by using NULL , in this we have used ' UNION SELECT NULL,NULL--; 
step 2 : identifying the administrator password, in this we have used ' UNION SELECT USERNAME,PASSWORD FROM USERS--; 
NOTE: TABLES AND COLUMNS ARE ALREADY MENTIONED 

payload: ' UNION SELECT USERNAME,PASSWORD FROM USERS--; 

impact: Knowing the number of columns is the first step in a UNION attack. Without this an attacker cannot extract data. This information allows an attacker to build further payloads to dump tables, credentials, and sensitive data from the database. 

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code 

What I Learned: 
In this lab the table and column names were provided. In real world targets I would need to enumerate them first using information_schema.tables and information_schema.columns before extracting data.

Mistakes I Made: i had to make trail and error to get the info of columns
