Title : Stored XSS into anchor href attribute with double quotes HTML-encoded

Vulnerability: cross site scripting

Severity: High

Attack Surface: This lab contains a stored cross-site scripting vulnerability in the comment functionality

What Happened:
The website field in the comment form accepts a URL
That URL is placed inside an href attribute
javascript:alert(1) executes JavaScript when the link is clicked

Payload :javascript:alert(1)

impact:
Attacker can able to steal the session cookie and can able to login as an user or administrator and take over the control of the website

Remediation:
Encode all user supplied output before rendering in HTML. 
Both angle brackets AND quotes must be encoded. Use a 
security library to encode all special characters including 
< > " ' to prevent attribute injection.
validate that URLs start with http:// or https:// only. Reject javascript: protocol entirel


What I Learned:
I learned that href attributes accept the javascript: protocol 
which allows JavaScript execution when a user clicks the link. 
Developers often forget to validate URL schemes and only focus 
on encoding special characters.

Mistakes I Made: i had to try trail and error to identify which one is not encoded.