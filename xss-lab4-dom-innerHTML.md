Title : DOM XSS in innerHTML sink using source location.search

Vulnerability: cross site scripting

Severity: High

Attack Surface: This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality

What Happened:
Source: location.search
Sink: innerHTML
In this lab i have found the vulnerable code, which is directly injecting user input to the sink(innerHTML), so if the user injecting <img src=x onerror=alert(1)> this payload , it will send this to sink and processed it will trigger the payload.

Payload: <img src=x onerror=alert(1)>

impact:
 Attacker can able to steal the session cookie and can able to login as an user or administrator and take over the control of the website

Remediation:
 Encode user supplied output before rendering it in HTML. Use HTML entity encoding so that < becomes < and > becomes preventing the browser from treating input as executable code.

What I Learned: i have learned about DOM xss little depth, like source and sink and how user input is sending to the sink and help me understand context like where i have to escape from qoutes.

Mistakes I Made: i hade to make trail and error to understand DOM xss and still lacking in DOM xss skill
