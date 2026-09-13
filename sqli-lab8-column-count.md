Title: SQL injection UNION attack, determining the number of columns returned by the query

Vulnerability: sql injection

Severity: High

Attack Surface:SQL injection vulnerability in the product category filter

What Happened: SQL injection vulnerability in the product category filter and in this we have to indetify how many columns will return for that i have used this payload ' UNION SELECT NULL,NULL,NULL-- and here each NULL represents each columns and i resolved the lab.

Payload:' UNION SELECT NULL,NULL,NULL--

Impact: Knowing the number of columns is the first step in a UNION 
attack. Without this an attacker cannot extract data. This 
information allows an attacker to build further payloads to 
dump tables, credentials, and sensitive data from the database.

Remediation:Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code

What I Learned:
i have learned how to use NULL and with that how to construct the payload based on the context.

Mistakes I Made:
 i had to make trail and error to get the info of columns
