Title : Reflected XSS into attribute with angle brackets HTML-encoded

Vulnerability: cross site scripting

Severity: High

Attack Surface: reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded

What Happened:
in the Lab search functionality is vulnerable xss, First i have checked test123 payload and it got reflected in the browser, later i tried <u>test123 and it got encode the <angle brackets> so i tried with " is it not encoded so i tried the " autofocus onfocus="alert(1) and it got reflected and succesfully lab solved.

Payload :" autofocus onfocus="alert(1)

impact:
Attacker can able to steal the session cookie and can able to login as an user or administrator and take over the control of the website

Remediation:
Encode all user supplied output before rendering in HTML. 
Both angle brackets AND quotes must be encoded. Use a 
security library to encode all special characters including 
< > " ' to prevent attribute injection.


What I Learned:
 learned how xss is triggered when the user input is encoded how to bypass the encodings sometime developer made mistakes only encoding the angle brackets leaving " so that i tried " and it got worked.

Mistakes I Made: i had to try trail and error to identify which one is not encoded.