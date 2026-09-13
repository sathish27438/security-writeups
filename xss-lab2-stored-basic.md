Title : Stored XSS into HTML context with nothing encoded

Vulnerability: cross site scripting

Severity: High

Attack Surface: stored cross-site scripting vulnerability in the comment functionality

What Happened:
in the Lab comment functionality is vulnerable xss, First i have checked test123 payload and it got stored and reflected in the browser, later i tried <u>test123 and it perfectly injected and then later i used <script>alert(1)</script> and it got triggered.Unlike reflected XSS, the payload is stored in the database 
and triggers automatically for every user who visits the page.

Payload : <script>alert(1)</script>

impact:
Attacker can able to steal the session cookie and can able to login as an user or administrator and take over the control of the website

Remediation:
Encode user supplied output before rendering it in HTML.
Use HTML entity encoding so that < becomes < and > becomes
preventing the browser from treating input as executable code.

What I Learned:i had to make trail and error to get know xss is possible

Mistakes I Made: Initially used alert(!) which is invalid JavaScript. Correct syntax is alert(1).
