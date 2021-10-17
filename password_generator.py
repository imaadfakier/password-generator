#Password Generator Project

from random import randint, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#password = ""
letters_to_use = ""
symbols_to_use = ""
numbers_to_use = ""
random_password = ""

for letter in range(0, nr_letters):
  #password += letters[random.randint(0, len(letters) - 1)]
  #password += letters[randint(0, len(letters) - 1)]
  letters_to_use += letters[randint(0, len(letters) - 1)]

for letter in range(0, nr_symbols):
  #password += symbols[random.randint(0, len(symbols) - 1)]
  #password += symbols[randint(0, len(symbols) - 1)]
  symbols_to_use += symbols[randint(0, len(symbols) - 1)]

for letter in range(0, nr_numbers):
  #password += numbers[random.randint(0, len(numbers) - 1)]
  #password += numbers[randint(0, len(numbers) - 1)]
  numbers_to_use += numbers[randint(0, len(numbers) - 1)]

password = letters_to_use + symbols_to_use + numbers_to_use

a_list = list(password)
shuffle(a_list)

for char in a_list:
  random_password += char

print(f"Password to use: {random_password}")
