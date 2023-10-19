"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print()

#define a class called Person with attributes name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #method to introduce the person
    def intro(self):
        print("Hello, my name is", self.name, "and my age is", self.age)

#create a Person object with the name "Caleb" and age 17
person_intro = Person("Caleb", 17)

#call the intro method to introduce the person
person_intro.intro()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()

#define a base class Animal with an empty speak method
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

#create a subclass Cat that overrides the speak method
class Cat(Animal):
    def speak(self):
        print("The Cat Meows") #prints

#create a subclass Dog that overrides the speak method
class Dog(Animal):
    def speak(self):
        print("The Dog Growls") #prints

#create a Cat object named Martha and a Dog object named Stevie
cat_object = Cat("Martha")
dog_object = Dog("Stevie")

#call the speak method on the Cat object
cat_object.speak()  #outputs "The Cat Meows"

#call the speak method on the Dog object
dog_object.speak()  #outputs "The Dog Growls"



    

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

#defines a class called BankAccount
class BankAccount:
    #initialize the class with attributes balance and owner
    def __init__(self, balance, owner):
        self.balance = balance  #set the balance attribute
        self.owner = owner      #set the owner attribute

    #method to display the current balance
    def balancez(self):
        print("The balance is", self.balance) #prints the current balance

    #method to deposit money into the account
    def deposit(self, dep):
        self.balance = self.balance + dep  #update the balance with the deposit
        print("Your New balance is", self.balance) #prints the current balance

    #method to withdraw money from the account
    def withdraw(self, wdraw):
        self.balance = self.balance - wdraw  #update the balance after withdrawal
        print("Your New balance is", self.balance) #prints the current balance

#create an instance of the BankAccount class for Caleb
calebs_bank = BankAccount(1000, "Caleb") 

#call the balancez method to display the initial balance
calebs_bank.balancez()

#call the deposit method to add $500 to the account
calebs_bank.deposit(500)

#call the withdraw method to take out $750 from the account
calebs_bank.withdraw(750)

