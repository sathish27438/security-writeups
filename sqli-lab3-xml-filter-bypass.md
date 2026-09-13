Title: SQL injection with filter bypass via XML encoding 
Vulnerability : sqli 
Severity: High
Attack Surface: stock check feature 

What Happened: there is feature for check the stocks it will fetch the result from database and it is user controllable,so Attacker can modify the user value with UNION sql query, when it was excuted it will give other tables values, for example UNION SELECT username||'~'||password FROM users-- it will fetch the username and password from the users table, Before extracting data we need to identify how many 
columns the original query returns. We do this by injecting NULL values one at a time until the query succeeds.

payload: <storeId><@dec_entities>UNION SELECT username||'~'||password FROM users--</@dec_entities></storeId> 

Remediation:Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned: I have learned about bypassing the WAF which will inspect the application layer once we obfusticate the payload we can easily bypass the WAF. 

Mistakes I Made: Mistakes I Made: I confused columns with tables when explaining NULL. NULL is used to identify how many columns the original query returns, not how many tables exist in the database.
