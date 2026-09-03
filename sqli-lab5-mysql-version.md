Title: SQL injection attack, querying the database type and version on MySQL and Microsoft

Vulnerability: sql injection (sqli)

Severity: High

Attack Surface: SQL injection vulnerability in the product category filter

What Happened: In this Lab we have the retirive the database version to do that we have to perform the sql injection in category filter , to perform Using a UNION attack we combined the original query results with a second query using @@version to retrieve the MySQL database version string.

Payload: ' UNION SELECT @@version, NULL-- -

Impact:

Which known CVEs apply to that exact version

Which attack techniques work on that database

Whether the database is unpatched and exploitable

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned: i have learned for diffrent database we have to use diffrent querys, i have Learned the NULL uses properly, like NULL will help us to identify the columns in the tables and also i learned idefying the coulumn data types with this SQL query ' UNION SELECT @@version, NULL-- -

Mistakes I Made: it is hard for me to detect the database query, for this i have to research and i have to test it here
