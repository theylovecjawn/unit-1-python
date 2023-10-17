try: #Using try because when the user inputs a string it gives an error
    age = int(input('Enter your age: ')) #asks the user for a age input
except: #runs when the error occurs
    print("Hey! That isn't a valid number Please try again.") #prints after the error occurs

faveNum = int(input('What is your favorite number: ')) #asks the user for a int input for thier favorite number

if age <= 21: #if statement runs when the age is  less than or equal to  21
 print('You are not allowed to enter, you are too young.') #prints that they are too young
else: #runs when the if statement is false
 print('Welcome, you are old enough.') #prints you are able to come through because they are old enough

try: #Using try because when the user inputs 0 for the faveNum it will cause an error.
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum) #prints the fun fact and divides
except: #if the error runs then this happens
    print("Hey! I am sorry we can't divide this by 0.") #Prints user friendly error