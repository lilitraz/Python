# 1.

valid_credentials = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange'
}

username = input("name: ")
passw = input("password: ")

if username in valid_credentials and valid_credentials[username] == passw:
    print("welcome!")
else:
    print("INTRUDER ALERT")



