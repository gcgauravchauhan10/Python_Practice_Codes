##################################
####.     OOPS.              #####
##################################

#Object oriented programming
#Objects used in code to simulate real world scenarios
a=20
b=30
sum=a+b
print(sum)

#Functions - reduce redundancy, reusability increases
#Class > Object > Student
class Student:
    name = "Gaurav Chauhan"
#creating object (instance)
Object_school=Student()
print(Object_school)    
print(Object_school.name)

#Factory and cars example
class Cars:
    Colour = "Blue"
    Brand = "Mercedes"
print(Cars.Colour)
Object_car=Cars() #objects are also called instance or instances of class
print(Object_car.Colour)
print(Object_car.Brand)

#constructor - All classes have a function called _init_o. Python calls it by default even if we dont create it
class Student:
    name = "Gaurav Chauhan"
    def __init__(self):
        print("Adding New Student in Database")
S1 = Student()
print(S1)

class Student:
    def __init__(self):   #default constructor
        pass
    def __init__(self,fullname,marks,grade):   #Parameterized constructor - we can write anything like abcd in place of self. Any other word in place of fullname is also ok
        self.name = fullname
        self.marks=marks
        self.grade=grade
        print("Adding New Student in Database",self.name)
S1 = Student("Karan",80,"B")
S2 = Student("Aarav",98,"A")
print(S1.name,S1.marks,S1.grade)
print(S2.name,S2.marks,S2.grade)

#Attributes are of two types a. Class Attributes b. instance attributes
#If same name attribute is present in class and instance, the one getting precedence is instance attribute
class Student:
    college = "Ramjas College" #Class attribute
    name = "Anonymous"
    def __init__(self):
        print("Adding New Student in Database")
    def __init__(self,fullname,marks,grade,college):   #Parameterized constructor - we can write anything like abcd in place of self. Any other word in place of fullname is also ok
        self.name = fullname                    #Instance attributes
        self.marks=marks
        self.grade=grade
        self.college=college
    #Methods are the functions that belong to objects
    def welcome(self): #This is how a method is being defined
        print("Welcome Student")
    def get_marks(self):
        return self.marks
S1 = Student("Karan",80,"B","Ramjas Instance")
S2 = Student("Aarav",98,"A","Ramjas Instance")
print(S1.college,S1.name,S1.marks,S1.grade)
print(S2.college,S2.name,S2.marks,S2.grade)
S1.welcome()
S1.get_marks()
print(S1.get_marks())

#Practice questions
#Create a student class that takes name and marks of 3 subjects as arguments in constructor.
#Then create a method to print the average
class Students:
    print("Hello World")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg_marks(self):
        sum = 0
        n = 0
        for val in self.marks:
            sum += val
            n +=1
        avg_marks = sum / n
        print("Hi", self.name, "your average marks across subjects are",avg_marks)
ST1=Students("Aarav",[97,95,92,99])
ST2=Students("Ahana",[98,95,91,89])
print(ST1.marks)
print(ST2.marks)        
ST1.avg_marks()
ST2.avg_marks()

ST2.name="Shanvi"
ST2.avg_marks()

#Static methods - Methods that dont use the self parameter (work at class level)
class Student:
    @staticmethod #decorator
    def college():
        print("ABC College")
Student.college()

#IMPORTANT CONCEPTS
#Abstraction (hidden / unclear) - Hiding the implementation details of a class and only showing the essential features to the user.
class Car:
    def __init__(self):
        self.accelerator=False
        self.brk = False
        self.clutch = False
    def Start(self):
        self.clutch = True
        self.accelerator = True
        print("car started..")
car1 = Car()
car1.Start()
#Encapsulation - Wrapping data and functions into a single unit (object)
#Inheritence - 
#Polymorphism

#Practice
#Create Account class with 2 attributes - balance and account no.
#Create methods for debit, credit and printing the balance
class Account:
    def __init__(self,bal,acct_num):
        self.balance=bal
        self.accountnumber=acct_num
    def debit(self,amt):
        self.balance -= amt
        print("Rs.", amt, "deducted. Your new account balance is",self.balance)
    def credit(self,amt):
        self.balance += amt
        print("Rs.",amt,"credited. Your new account balance is",self.balance)
    def get_balance(self):
        return self.balance
S1 = Account(5000,"ABC1234")
S1.balance

S1.debit(500)
S1.credit(1000)
S1.get_balance()





