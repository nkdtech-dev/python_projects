# Password Generator #
from random import choice, choices, randint,randrange, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator BY DELEO!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print("In total you have a password of",nr_letters+nr_symbols+nr_numbers,"character")

#Easy Level password
password = ""

for char in range(nr_letters):
    password += choice(letters)

for char in range(nr_symbols):
    password += choice(symbols)

for char in range(nr_numbers):
    password += choice(numbers)
print(f"Your Easy Password is:'{password}")

#Hard Level
password_list = []

for char in range(nr_letters):
    password_list.append(choice(letters))

for char in range(nr_symbols):
    password_list += choice(symbols)

for char in range(nr_numbers):
    password_list += choice(numbers)

# print(password_list)
shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your Hard password is: {password}")