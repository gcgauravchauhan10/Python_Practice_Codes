#Functions and recursions - Functions are equivalent to SAS macros
def calc_sum(a,b): #Inputs known as parameters or params
    sum=(a+b)/2
    print(sum)
    return sum  #return is used for sending the output back


a=100
b=250
calc_sum(a,b) #calling the function

calc_sum(70,249)

def calc_sum(a,b):     #def is function definition values passed into params are called arguments
    return a+b

Sum=calc_sum(134,34)
print(Sum)

def ph():
    print("It's a good day.")

ph()
print(ph()) #this will give none if the function is not returning anything

def ph():
    return "It's a good day." #Not the function is returning a value so function output can be printed

print(ph())

def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg

print("Average is ",calc_avg(10,20,60))

#Types of functions 1. Built in (like print, sum etc.) 2. User defined functions
print("apna college","\n""gaurav Chauhan")
print("apna college")
print("gaurav chauhan")
print("apna college",end="gc")
print("gaurav chauhan")

#Assigning default values to the parameters in case we dont want to pass any values
def cal_prod(a=1,b=1): #non default argument should follow default argument in case one is to be default
    return a*b

cal_prod()
cal_prod(10,5)

#WAF to print the length of a list (list is the parameter)
def list_length(list1):
    return (len(list1))

list_=[3,5,2,7,8,9,10]
list_length(list_)

#WAF to print the elements of a list in a single line (list is the parameter)
def list_length(list1):
    for i in range(0,len(list1)):
        print(list1[i],end=" ")

list_=[3,5,2,7,8,9,10]
list_length(list_)

#WAF to find the factorial of n (n is the parameter)
def factorial1(n):
    i=1
    fact1=1
    while i <= n:
        fact1 *= i
        i +=1
    
    return fact1

factorial1(5)

#WAF to convert USD into INR
def convert_to_rupee(USD):
    Amount=92*USD
    return Amount

convert_to_rupee(75)

#Recursion
#When a function calls itself repeatedly
#print n to 1 backwards
def show(n):
    if n==100: #a base case is must to stop the recursion
        return
    print(n)
    show(n+1)
show(10)

#recursion through factorial
def fact1(n):
    if n==0 or n==1:
        return 1
    else:
        return fact1(n-1) * n
fact1(6)

#Write a recursive function to calculate the sum of first n natural numbers
def sum_n(n):
    if n==0:
        return 0
    else:
        return sum_n(n-1) + n
sum_n(10)

#Write a recursive function to print all elements a list
def print_list(list,idx=0):
    if(idx == len(list)):
            return
    print(list[idx])
    print_list(list,idx+1)

list1=["Apples","Oranges","Mangoes","Pinapples"]
print_list(list1)

####practice - revision######
def factorial1(a):
        if a==1 or a==0:
            return 1
        else:
            return factorial1(a-1) * a
factorial1(5)
####practice - revision ends#####



