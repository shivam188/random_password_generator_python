import random

def pass_generator(n):
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$_"
    for i in range(n):
        password = password + random.choice(characters)
    return password

print("\n====== Random Password Generator ======")
num = int(input("Enter the length of Password : "))
pw = pass_generator(num)
print("Password is : "+pw)
