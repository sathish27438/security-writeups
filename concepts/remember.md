## Sqli injection remember
## 1. in xml use escaped entities
 I realized my mistake: the XML format prohibits some characters, including the apostrophe. To include them, you have to enter apostrophes as escaped entities. Instead of <MainAccount>123456'</MainAccount>, I had to use <MainAccount>123456&apos;</MainAccount>. The server immediately returned a database error message - I was on the right path!
## 2. User-Agent: header. 
 sometimes the database stores the user-agent to identify the user session, so better test sqli injection there also.