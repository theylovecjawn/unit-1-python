"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def sqaure_num(x): #creation of the sqaure_num function  
    return x**2 #gives the value back as the number sqaured
assert sqaure_num(6) == 36 #Checks the value of 6 sqared to see if it returns a error
try: #uses try as to keep it going even after the error occurs
    assert sqaure_num(2) == 6 #Checks the value of 2 sqared to see if it returns a error
except: #Except is needed for every single try for it to be able to run
    print("This assert is wrong") #if it is wrong this is prints

print(sqaure_num(2)) #prints the square number of 2 calling the sqaure_num function

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area_rect(z, y): #creation of the area_rect function 
    return z * y # gives back z * y

assert area_rect(2, 5) == 10 #Checks the value of 2 X 5 to see if it returns a error
try: #uses try as to keep it going even after the error occurs
    assert area_rect(6, 10) == 70 #Checks the value of 6 X 10 to see if it returns a error
except: #Except is needed for every single try for it to be able to run
    print("This assert is wrong") #if it is wrong this is prints

print(area_rect(3, 6)) #prints the area calling the function


"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def cel_converter(ded): #Creation of the cel_converter function
    g = ded * 1.8 #g variable which holds the ded variable given and 1.8 multiplied together
    h = g + 32 #adds 32 to the and sets the value to the h 
    return h #returns the h value 

assert cel_converter(68) == 20 #Checks the value of 68 F --> C to see if it returns a error
try: #uses try as to keep it going even after the error occurs
    assert cel_converter(20) == 6 #Checks the value of 20 F --> C to see if it returns a error
except: #Except is needed for every single try for it to be able to run
    print("This assert is wrong") #if it is wrong this is prints

print(cel_converter(24)) #prints the value from cel. to far. of the value 24
    


"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def average(q): #Creation of average function
   total = sum(q) #total is equal to the sum of all the numbers in the given paramter
   return total / len(q) # gives back the mean (all the numbers added up then divided by the number of the rest)

assert average([3,4,5,6]) == 4.5 #Checks the value of the mean for the list 3,4,5,6 to see if it returns a error
try: #uses try as to keep it going even after the error occurs
    assert average([9,4,3,2]) == 2 #Checks the value of the mean for the list 9,4,3,2 to see if it returns a error
except: #Except is needed for every single try for it to be able to run
    print("This assert is wrong") #if it is wrong this is prints

q = [1,2,3,4,5] # sets q to the list 1,2,3,4,5
print((average(q))) #prints the average using the function and giving it the q
    