#Password Generator

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '(', ')', '?']

print('Welcome to the RPassword Generator')

nr_letters = int(input('How many letters would you like your password to have?\n'))
nr_numbers = int(input('How many numbers would you like your password to have?\n'))
nr_symbols = int(input('How many symbols would you like your password to have?\n'))

#print(f'{nr_letters} letters, {nr_numbers} numbers, {nr_symbols} symbols')

def passwordGenerator1():
    password = ''

    # letters
    for count in range(1, nr_letters+1):
        password += random.choice(letters)

    # numbers
    for count in range(1, nr_numbers+1):
        password += random.choice(numbers)


    # symbols
    for count in range(1, nr_symbols+1):
        password += random.choice(symbols)

    # shuffle password
    passwordAsList = list(password)
    random.shuffle(passwordAsList)
    password = ''.join(passwordAsList)

    print(password)


for i in range(1, 6):
    passwordGenerator1()
