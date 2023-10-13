import datetime #importing the datetime module
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print(datetime.datetime.now()) #Takes the date and time and prints it

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print(datetime.datetime.now()) #Takes the date and time and prints it

now = datetime.datetime.now() #Sets a cariable to the current time
print(now.strftime("%m/%d/%Y")) #prints the date in MM/DD/YYYY format

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
def convert(date_time): #creation of the function converts the string to a datetime
    format = '%b %d %Y %I:%M%p' #sets the format 
    datetime_str = datetime.datetime.strptime(date_time, format) #uses the strptime  to set the format
 
    return datetime_str #returns datetime_str

date_time1 = 'Dec 4 2018 10:07AM' #sets a variable for the first date
date_time2 = 'Oct 7 2020 2:07AM'#sets a variable for the second date

x = convert(date_time1) #uses the convert function to convert
y = convert(date_time2) #uses the convert function to convert

print(y - x) #subtracts the second one from the first date
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
from datetime import date #Imports the date from the datetime module
def age(birthDate): #creates function that determines the age based on the given year/day/month
    today = date.today() #sets todays date
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) #sets the age variable
 
    return age #returns age
def convert2(date_time): #creation of the function converts the string to a datetime
    format = '%Y/%d/%m' #sets the format to yyyy/dd/mm
    datetime_str = datetime.datetime.strptime(date_time, format) #uses the strptime  to set the format
 
    return datetime_str #returns datetime_str   
birthday = input('Please input your birth day (YYYY/DD/MM): ') #asks user for an input i the yyyy/dd/mm format

d = convert2(birthday) #calls the convert2 function and sets the input to a variable

print(age(d)) #prints the age 