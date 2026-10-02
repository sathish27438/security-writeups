for i in range(150):
    if i % 3 == 0:
        print("wiener")
    else:          
     print("carlos")

print("\n")
print("###############" + "Printing Passwords...." + "##########################")
print("\n")
print("printing passwords")
print("\n")

with open("tools/password.txt", encoding="utf-8") as f:
    passwords = [line.strip() for line in f if line.strip()]


password_index = 0
for i in range(150):
    if i % 3 == 0:
        print("peter")
    else:
        print(passwords[password_index])
        password_index += 1