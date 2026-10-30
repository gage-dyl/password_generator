#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User
import random

#Flower Box Section

#########################################################
#                                                       
# Name:  Gage Doyle                          
# Date:  10/29/2026
# Program Description:
#
# This is a program to create a password for a user based                                                    
# on the user input entered  
#                                                          
#########################################################

#Variables section

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
SPECIAL_CHARACTERS = '!@#$%^&*?~'
NUMBERS = '1234567890'
YES_LIST = ['YES','Yes','yes','y','Y']

length_of_password = 0
use_special_characters = False
use_numbers = False
password = ''
count = 0
letters = 0
sp_char = 0
nums = 0

#Input section

while True:
    length_of_password = input("Please enter a number (int) from 8 to 16 for a password length: ")
    if length_of_password.isnumeric():
        length_of_password = int(length_of_password)
        if length_of_password in range(8,17,1):
            break
        else:
            continue
    else:
        continue

answer = input("Do you want special characters in your password: ")

if answer in YES_LIST:
    use_special_characters = True

answer = input("Do you want numbers in your password: ")

if answer in YES_LIST:
    use_numbers = True

#Process section

while count < length_of_password:
    randomNumber = random.randrange(0,52,1)
    pwChar = ALPHABET[randomNumber]
    password = password + pwChar
    count = count + 1

    if use_special_characters and count < length_of_password:
        randomNumber = random.randrange(0,11,1)
        pwChar = SPECIAL_CHARACTERS[randomNumber]
        password = password + pwChar
        count = count + 1

    if use_numbers and count < length_of_password:
        randomNumber = random.randrange(0,11,1)
        pwChar = NUMBERS[randomNumber]
        password = password + pwChar
        count = count + 1

for item in password:
    if item in ALPHABET:
        letters = letters + 1
    elif item in SPECIAL_CHARACTERS:
        sp_char = sp_char + 1
    else:
        nums = nums + 1

#Output section

print(date.today())
print(getpass.getuser())
print('-------------------------------------------------------------------------------------------')
print("Your password is " + password)
print("Your password is " + str(len(password)) + " characters long.")
print("Your password has " + str(letters) + " letters.")
print("Your password has " + str(sp_char) + " special characters.")
print("Your password has " + str(nums) + " numbers.")
