Title: SQL injection UNION attack, finding a column containing text

Vulnerability: sql injection

Severity: High

Attack Surface: SQL injection vulnerability in the product category filter

What Happened: in this lab we have to identify how columns and returning and which column using text data type. step 1: identifying the columns by using NULL , in this we have used ' UNION SELECT NULL,NULL,NULL--; step 2: identifying the text data type columns by passing string in the sql query, in this Lab i used ' UNION SELECT NULL,'a',NULL--;
Payload: ' UNION SELECT NULL,'HM3Bw6',NULL--;

Impact: Knowing the number of columns is the first step in a UNION attack. Without this an attacker cannot extract data. This information allows an attacker to build further payloads to dump tables, credentials, and sensitive data from the database.

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code

What I Learned: i have learned how to use NULL and with that how to construct the payload based on the context. 

Mistakes I Made: i had to make trail and error to get the info of columns
