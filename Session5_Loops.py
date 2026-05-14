####################
####LOOPS###########
####################
#While loops and for loops

a="Hello"
print(a)

# while True:
#     print(a)
cnt=1       #Iterator
while cnt <=10 :      #Iterations
    print(a)
    cnt += 1

print(cnt)

i=1
while i<=100000:
    print("Gaurav",i)
    i +=1

i=1
while i<=5:
    i=i*i+1
    print(i)
    i +=1
print(i)
    
#reverse loop
i=5
while i>=0:
    print(i)
    i -=1
print("Loop Ended")

#Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i +=1

#Print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i -=1

#Print the multiplication table for a number 11
i=1
while i<=10:
    print(11*i)
    i +=1

i=1
while i<=10:
    print(43*i)
    i +=1

j=1
while j<=10:
    print(j*j)
    j +=1

#Search for a number x in this tuple using loop:
tup1=(1,4,9,16,25,36,49,64,81,100)
print(len(tup1))
a=81
i=0
found=False
while i <= len(tup1) - 1:
    if tup1[i] == a:
        print (a,"is there in the tuple")
        found=True
        break
    i +=1
if not found:
    print(a,"was not found")    

#practice questions start
i=1
while i<=10:
    print(i*i)
    i +=1

tup1=(1,4,9,16,25,36,49,64,81,100)
z=100
i=0
found=False
while i <= len(tup1)-1:
    if tup1[i] == z:
        print(z, "is in the list")
        found=True
        break
    i +=1
if found==False:
    print(z,"cant be found")
#practice questions end

#Break and Continue keywords
#Break - To terminate the loop
i=1
while i<=5:
    print(i)
    if i==3:
        break
    else:
        print("Finding...")
    i +=1

#Continue - terminates execution in the current iteration & continues execution of the loop with the next iteration
i=1
while i<=10:
    if i == 3:
        i +=1
        continue
    print(i)
    i +=1

# FOR LOOP IN PYTHON - Used for traversing on a data type like string, list, tuple, set etc.
list1=[1,2,3,4,6,5]

for val in list1:
    print(val)

veggies=["potato","brinjal","ladyfinger","carrot"]
for val in veggies:
    print(val)

str="apnacollege"
for char in str:
    if char == "c":
        print(char,"found")
        break
    print(char)
else:
    print("not found")
#an optional else: can be used along with a for loop to provide with a diff output

#Print the elements of the following list using a loop:
list1=[1,4,9,16,25,36,49,64,81,100]
for val in list1:
    print(val)

tuple1=(1,4,9,16,25,36,49,64,81,100)
x=65
for val in tuple1:
    if val==x:
        print(x,"found")
        break
else:
    print(x,"not found") 


#Range() Range function returns a sequence of numbers, starting from 0 by default and increments by 1 (by default)
#, and stops before a specified number
for el in range(1,5):
    print(el)

print(range(5))

seq=range(10)
for i in seq:
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,10,2): #range(start,stop,incrementby) 
    print(i)

#Practice questions
#Print numbers from 1 to 100
for i in range(1,101):
    print(i)
#Print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#Print the multiplication table of a number n
Table=7
for i in range(1,11):
    print(Table*i)

#Practice - WAP to find the sum of first n numbers (using while)
n=15
sum=0
i=0
while i <= n:
    sum=sum+i
    print(sum)
    i +=1

#WAP to find factorial of first n numbers (using for)
fact=1
for val in range(1,6):
    fact=fact*val
print(fact)






