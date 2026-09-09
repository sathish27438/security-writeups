Title : Reflected XSS into HTML context with nothing encoded

Vulnerability: cross site scripting

Severity: High

Attack Surface: Reflected XSS into HTML context with nothing encoded

What Happened:
in the Lab search functionality is vulnerable xss, First i have checked test123 payload and it got reflected in the browser, later i tried <u>test123 and it perfectly injected and then later i used <script>alert(1)</script> and it got triggered.

Payload : <script>alert(1)</script>

impact:
Attacker can able to steal the session cookie and can able to login as an user or administrator and take over the control of the website

Remediation:
Encode user supplied output before rendering it in HTML.
Use HTML entity encoding so that < becomes < and > becomes
> preventing the browser from treating input as executable code.

What I Learned:
 learned how xss is triggered when the user inject javascript through script

Mistakes I Made: Initially used alert(!) which is invalid 
JavaScript. Correct syntax is alert(1).
