#Py Password Generator 
import random
print("Welcome to the PyPassword Generator!")
# Create a list of letters, symbols, and numbers
letters_list = ['a', 'b', 'c', 'd', 'e', 'f ', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', '', '*', '(', ')', '_', '+', '=', '/',]
symbols_list = ['!', '@', '#', '$', '%', '^ ', '&', '*', '(', ')', '_', '+', '=', '/',]
numbers_list = ['0', '1', '2', '3', '4', '5 ', '6', '7', '8', '9', '0']

# Get the number of letters, symbols, and numbers from the user
num_letters = int(input("How many letters do you want in your password : "))
num_symbols = int(input("How many symbols do you want in your password : "))
num_numbers = int(input("How many numbers do you want in your password : "))

# Create empty lists to store the selected letters, symbols, and numbers
selectL = []
selectS = []
selectN = []

# Generate random letters, symbols, and numbers and add them to the respective lists
for i in range(num_letters):
    random_letter = random.choice(letters_list)
    selectL.append(random_letter)

for i in range(num_symbols):
    random_symbol = random.choice(symbols_list)
    selectS.append(random_symbol)

for i in range(num_numbers):
    random_number = random.choice(numbers_list)
    selectN.append(random_number)

# Combine the selected letters, symbols, and numbers into a single list
select = selectL + selectS + selectN

# Shuffle the list to create a strong password
random.shuffle(select)

# Convert the list to a string and print the password
password = ''.join(select) #convert list into string
print("Your strong password is:", password)