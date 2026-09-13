Title: SQL injection attack, querying the database type and version on Oracle 

Vulnerability: sqli(sql injection) 

Severity: High 

Attack Surface: vulnerability in the product category filter 

What Happened: The category parameter was vulnerable to SQL injection.The solution for this Lab to retrive the ORACLE database version to do that we are using UNION to combine  query results and retrive the verion by using the below ' UNION SELECT banner,NULL FROM v$version-- 


Payload: ' UNION SELECT banner,NULL FROM v$version--

Impact: We can get the database version with that we can able to Known CVE for that version

* Known CVEs for that version
* Identify if database is unpatched
* Target specific exploits against that version
* RCE possibility if critical CVE exists


Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned: i have learned for diffrent database we have to use diffrent querys, i have Learned the NULL uses properly, like NULL will help us to identify the columns in the tables and also i learned idefying the coulumn data types with this SQL query' UNION SELECT 'a',NULL FROM dual--.
 Mistakes I Made: Initally i tried the UNION query which will only works on postgres and mysql later i get know for oracle we have to modify the query
