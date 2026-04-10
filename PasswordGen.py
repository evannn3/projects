import random
import string
import json
import re
import os
chars = string.ascii_letters + (string.digits * 4) + string.punctuation
file_name = "f.json"
thing = input("What would you like to do? (1/2)\n"
 "1: Generate password\n"
 "2: View passwords\n"
 "Enter choice: ")
f = ""
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        try:
            data = json.load(file)
        except:
            data = {}
else:
    data = {}
if thing == "1":
    length = int(input("Enter the length of the password: "))
    while True:
        f = ""
        for i in range(length):
            j = random.choice(chars)
            f += j
        print("Password: " + f)
        save = input("Would you like to save this password (y/n/r)?\n"
                     "y = Yes\n"
                     "n = No\n"
                     "r = Retry\n"
                     "Enter choice: ")
        if save == "y":
            title = input("Enter the title of the password: ")
            data[title] = f
            with open(file_name, "w") as file:
                json.dump(data, file)
                print("Password saved!")
            break
        elif save == "n":
            print("Goodbye!")
            break
        elif save == "r":
            continue
        else:
            print("Invalid input, try again.")
elif thing == "2":
    print("Loading file...")
    with open(file_name, "r") as file:
        openfile = json.load(file)
        stringfile = str(openfile)
        cleaner = re.sub(r"[{}']", "", stringfile)
        print(cleaner)
else:
    print("Choose 1 or 2 please.")





