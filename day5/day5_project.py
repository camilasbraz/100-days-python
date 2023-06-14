import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters= int(input("How many letters would you like in your password?\n")) 
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))

total_len = letters + symbols + numbers
n_letters = 0
n_numbers = 0
n_symbols = 0

password = ""

while len(password) < total_len:
    order =  random.randint(0,3)
    if order == 0 and n_letters < letters: 
        password += random.choice(letters_list)
        n_letters += 1
    if order == 1 and n_numbers < numbers: 
        password += random.choice(numbers_list)
        n_numbers += 1
    if order == 2 and n_symbols < symbols: 
        password += random.choice(symbols_list)
        n_symbols += 1

print(f"Your password is {password}")
