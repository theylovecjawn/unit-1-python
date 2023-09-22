import math
'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
number = int(input('Please enter a whole number: ')) # variable for the input number

if number % 2 == 0:
    print('This is a even number') # if the modulus is = 0 then it is a even number
else:
    print('This is an odd number') #If the modulus is not 0 then it will be an odd number
    

'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.
EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
number = int(input("Please give me a integer value: ")) #Made a variable for the input
if number > 0:  # if statement to show any value above 0 is positive
    print('This is positive')
elif number == 0: # elif statement to show any value below 0 is negative
    print("This is equal to 0")
else: # else statement to show any other values is equal to 0
    print ('This is a negative number')

'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''

var = max(16, 8, 72) # makes a variable which takes the biggest number out of the vaules.
print(var) # prints the biggest number

'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''

birth_year = int(input('Please give me your birth year: ')) #Creates variable for user input for their birth year

if birth_year % 4 == 0:
    print('CONGRATS YOU WERE BORN ON A LEAP YEAR!!!') #Prints if the year entered is divisible by 4
else:
    print('Sadly, you were not born on leap year.') #Prints only if it is not divisible by 4

'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''

abc = input('Please give me a letter in the alphabet: ') #creates inputs for the letter
if abc =='a' or abc == 'e' or abc == 'i' or abc == 'o' or abc == 'u': 
    print('This is a Vowel!!') #prints only if the value of the input is equal to a,e,i,o, or u.
else: 
    print('This is a consonant') #prints if the value is not equal to a,e,i,o, or u.


