"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
my_float = 4.0
my_int = int(my_float)

print(my_float)
print(my_int)

# I made a float variable, then made a into variable which converted the float variable into a int and then I printed them both.

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
number = int(input("Please give me a value: ")) #Made a variable for the input
if number > 0:  # if statement to show any value above 0 is positive
    print('This is positive')
elif number == 0: # elif statement to show any value below 0 is negative
    print("This is equal to 0")
else: # else statement to show any other values is equal to 0
    print ('This is a negative number')


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
theInt = int(input('Please give me a Integer: ')) # Made input for int
theFLoat = float(input('Please give me a Float(decimal): '))# Made input for float

add = theInt + theFLoat # did the addition of the int and float
subtract = theInt - theFLoat #did the subtraction of the int and float
mult = theInt * theFLoat # did the multiplication of the int and float
div = theInt / theFLoat # did the division of the int and float

print('These numbers added together is: ' + str(add)) #printing the value of the addition and changing the value to a string so it will work
print('These numbers subtracted is: ' + str(subtract))#printing the value of the subtraction and changing the value to a string so it will work
print('These numbers multiplied together is: ' + str(mult)) #printing the value of the multiplication and changing the value to a string so it will work
print('These numbers divied by one another is: ' + str(div)) #printing the value of the division and changing the value to a string so it will work


"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruits = {
    'apples': 6,
    'mangos': 2,
    'oranges': 9,
    'plumbs': 7,
    'grapes': 3

} #Creation of the dictionary 

print(fruits['mangos']) #printing with the syntax of Python

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

theList = "1,2,3,4,5,6" #creation of the list

theTuple = tuple(theList.split(",")) #Splicing with the commas so that It will convert to a string so that I can change it into a tuple.

print(theList) #Printing the list
print(theTuple) #Printing the converted tuple.
