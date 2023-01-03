"""password generator terminal base """
from random import shuffle, choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '<', '>', '@', '#', '$', '&', '%', '^', '*', '(', ')', ',', '.', '?', '/']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print("---------------------------welcome to password generator terminal--------------------")
number_letters = int(input("How many letters would you want in your password: "))
number_symbol = int(input("how many symbols would you want in your password: "))
number_numbers = int(input("how many numbers would you want in your password: "))
chosen_letters = [choice(letters) for i in range(0, number_letters)]
chosen_symbols = [choice(symbols) for j in range(0, number_symbol)]
chosen_numbers = [choice(numbers) for k in range(0, number_numbers)]

password_list = chosen_letters + chosen_symbols + chosen_numbers
password_string = ''
for m in range(0, len(password_list)):
    shuffle(password_list)
for l in password_list:
    password_string += l
print(f'your password is {password_string}')