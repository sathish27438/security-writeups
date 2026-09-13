Title : DOM XSS in document.write sink using source location.search

Vulnerability: cross site scripting

Severity: High

Attack Surface: DOM-based cross-site scripting vulnerability in the search query tracking functionality

What Happened:
in this LAB xss vulnerability in the search query tracking functionality, in this LAB document.write is an sink where javascript will execute, window.location.search is an source where user data will enter, to solve this we have tested with test123 and it will be reflected in <img src "test123" to excute this we have escape from src and inject our payload in this lab i used "><img src=x onerror=alert(1)> and it got reflected perfectly.

Payload : "><img src=x onerror=alert(1)>

impact: Attacker can able to steal the session cookie and can able to login as an user or administrator and take over the control of the website

Remediation: Encode user supplied output before rendering it in HTML. Use HTML entity encoding so that < becomes < and > becomes preventing the browser from treating input as executable code.

What I Learned: i have learned about DOM xss little depth, like source and sink how to escape from the attributes.

Mistakes I Made: i hade to make trail and error to understand DOM xss and still lacking in DOM xss skill
