'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
userInput = int(input('Please give me an integer: ')) # Asking the user for an input
if userInput > 10 and userInput % 2 == 0: #Checks to see if its greater than 10, and checks to see if its even and has no remainder
    print('True') #prints if true
else:
    print('False') #if false this prints

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = int(input('Please input your age: '))#Asks user to input thier age
student = input("Are you a student? (y = yes, n = no): ") #Checks if they are currently a student

if age < 18 or student == "y": #uses or to make true if 1 of them is correct
    print("The price is $10")#prints if 1 is true
else:
    print('The price is $20.')#prints if both are false

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits = ["apple", 'banana', 'mango', 'strawberry'] #Creates list for the fruits

favFruit = input('Please input your favorite fruit: ') # Asks user for their fruit and puts the inpiut into the variable favFruit

if favFruit in fruits:
    print('Yes, that fruit is in the list.') # Prints if it is in the list
else:
    print('No, that fruit is not in the list.') #Prints if it is not in the list


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year = int(input('Please input a valid year: ')) # Asks for a yea to be inputed

if year % 100 == 0 and year % 4 == 0: #takes the inputed year and confirms if it is a century year, Checks if the year is a leap year (divisible by 4)
    print('This is a century year, and a leap year.') #prints if true
else:
    print('This is not a century year, nor a leap year.')#prints if false

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
zoneUser = input("What is your zone? (a = Zone A, b = Zone B: ") #asks for the zone  they are in
orderWeight = float(input('Please input a weight for your order (kilograms): ')) #asks for the weight of the order

if zoneUser == "a": #works if the zone is a 
    print("Your order will be: $" + str(orderWeight * 5)) #calculates the price based on the Zone a
    if orderWeight < 0 :
        print("Sorry your weight is too low.") #prints if the weigth is below 0
elif zoneUser == "b": #works if the zone is b
    print("Your order will be: $" + str(orderWeight * 7)) #calculates the price based on the Zone a
    if orderWeight < 0 :
        print("Sorry your weight is too low.") #prints if the weigth is below 0

 
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

x = float(input('Please give me a value for side 1: ')) #gets value for side 1
y = float(input('Please give me a value for side 2: ')) #gets value for side 2
z = float(input('Please give me a value for side 3: ')) #gets value for side 3

if x == y == z: #Checks to see if all sides are equal
	print("This is an  Equilateral triangle")
elif x == y or y == z or z == x: #Checks to  see if 2 sides are equal
	print("This is an isosceles triangle")
else: #if no sides are equal this prints
	print("Scalene triangle")


