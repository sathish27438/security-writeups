Title : SQL injection attack, listing the database contents on non-Oracle databases

Vulnerability: sql injection

Severity: High

Attack Surface: SQL injection vulnerability in the product category filter.

What Happened:
we found that sql injection vulnerability is in category filter by passing ' . the we modified the payload query to identify how many columns are returning with NULL payload. later with the help information_schema we have listed the list schemas and here public is the application database. and the we found that there are two tables in the public database one for maintaing the users data and another one for maintaining the products, and we exctracted the columns from users tabel and the we retrived the username of admin and pssword from the users tabel.

Payload:
' UNION select username_yhtbdj, password_rqmhnc FROM users_uouqsx--

Impact:
An attacker can extract all usernames and passwords from the database giving full account takeover of any user including administrators.

Remediation:
Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned:
I have learned the informational schema completly by retriving the information database and tables and columns. And i have learned how to construct the payload for this.

* Counted columns ✅
* Listed schemas ✅
* Found target table ✅
* Extracted column names ✅
* Dumped credentials ✅
  

Mistakes I Made:
i made an lot of spelling mistakes in payload consttruction which leads to internal server error. and i did not know information_schema.schemata → databases and information_schema.tables → tables and information_schema.columns → columns then i later i googled it and i learned
