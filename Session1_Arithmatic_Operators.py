print ("Hello World")
print ("Aarav is stupid")
print ("I was kidding. Aarav is a smart kid")

a=15
print(a)
a=10
b=25
c=a+b
print(c)

import pandas as pd
name = "Shradha" #string
age=23
price=25.99
print(name, age, price)
print("my name is", name)
print("I am", age)
print("I bought tomatoes at Rs.",price,"per KG")
myname="Gaurav chauhan"
print(myname)
print(type(name)) #Type - data type
print(type(age))
print(type(price))
if age<60:     # Colon is used in place of then. post then condition can be in this line or next line
   category='Young'
else:
    category = 'Old'
print(category)

a=1000
b = 1500
c=b-a
print(c)

"""MULTI LINE COMMENT : My name is Gaurav and I am learning Python, 
I am enjoying it a lot. I am sure that I will
become a good programmer in future"""

print(a==b) # == is comparison operator and gives values True or False

if a!=b:    # != is not equal to operator
    c=b-a
else:
    c=b+a
print(c)

#Assignment operators
a=10
a=a+5
print(a)
a+=5 # a=a+5
print(a)
a=a-3
print(a)
a-=2 # a=a-2
print(a)
a*=2
print(a)
a**=3
print(a)
a//=2
print(a)
a%=1000 #   Remainder--  a=a%5000
print(a)

#TIPS : TO COMMENT MULTIPLE LINES IN ONE GO, SELECT THE LINES AND PRESS COMMAND + /
#Logical operators
a=10
b=20

#Relational operators
a=50
b=20
print(a==b) # False

print(a!=b) # True

#Logical operators
a=50
b=20
print(a>30 and b<30) # True and True = True
print(a>50 or b>30) # True and False = False
print(not a+b>60) # a+b=70, 70>60 is True, not True = False

#Type conversion - Type casting
a, b, c = 10, 20, 30.25
sum = a + b + c
print(sum) # 60.25 python automatically converts int to float as it is superior data

a,b,c = "2", 20, 30.25 # a is string, b is int, c is float. We cannot add these three as they are of different data types
sum=int(a)+b+c # TypeError: can only concatenate str (not "int") to str
print(sum)

a=3.14
a=str(a)
print(type(a)) # <class 'str'>

#Input in python
name = input("Enter your name: ")
print("Hello Mr", name)
print(type(name),name)
age = int(input("Enter your age: ")) #if we dont convert the input to int, it will be of type string and we cannot perform any mathematical operations on it
print("You are", age, "years old")
print(type(age), age)

a=40
b=20
c=sum(a,b) # sum is a built-in function in python which takes two arguments and returns their sum
print(c)

#Practice questions

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=a+b
# print(c)

from numpy import average


sq_side=20
sq_area=sq_side**2
print("Area=",sq_area)

import pandas as pd

# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# c=average([a,b])
# print("Average=",c)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a>=b)

