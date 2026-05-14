#=======================================
# Lists & Tuples =======================
#=======================================
#Lists and Tuples are Python sort of equivalents of Arrays

marks=[20.5,50.7,47.8,51.9,55.7,98] #Called list in python
print(type(marks))

#quite few list properties are similar to string
print(marks[0]) # Gives marks stored in the 0th position from left
print(marks[5])
print(marks[-1]) #Gives first value from last
print(len(marks))

#Python lists can store elements of different types unlike Java and C++

student=["Aarav",85,9,"Adarsh Nagar"]
#IMPORTANT: Strings are immutable in python, lists are mutable in python
print(student[0])

student[0]="Ahana"
print(student)

Student_Name="Shivay Chauhan"
print(Student_Name[0])
## Student_Name[0] = "C" #gives error 'str object does not support item assignment

#Slicing
marks=[87,64,33,95,76,89,77]
print(marks[1:6])
print(marks[-3:-1])

#List Methods - Strings, Lists and Tuples all may have similar / differnt methods
list=[2,4,3,5,6]
list.append(7)
print(list)

list.sort()
print(list)
list.sort(reverse=True)
print(list)

list1=["Banana","Lichi","Mango","Apple"]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list1.reverse() #reverses the original order
print(list1)

list1.insert(2,"Orange")
print(list1)

#List methods: Remove
list2=[2,1,7,7,3,4,3,8]
list2.remove(7) #Removes first occurance of the element
print(list2)
#List methods: pop
list2.pop(2) #removes element at the index
print(list2)

print(list2.count(3))
#list2.clear()
print(list2)

#Tuples - A built in data type that lets us create immutable sequence of values
#List is a mutable data type. Tuple is a immutable data type
tup=(2,4,3,2)
print(type(tup))
print(tup)

# tup[2]=5 This will give error as 'tuple' object does not support item assignment
tup1=()
print(type(tup1))
print(tup1)

tup2=(1) #single value without a comma is treated as integer, floating, boolean etc. but not tuple
print(type(tup2))
tup2=(1,)
print(tup2)
print(type(tup2))

tup=(1,3,2,4,5,5,4,2) 
tup.index(4) #This gives the index of the value put within brackets following order 0,1,2,3,4...
tup.count(4)

#Let's practice
#WAP to ask the user to enter names of their 3 favourite moves and store them in a list.
movie1=input("Enter fav movie 1:")
print(movie1)
movie2=input("Enter fav movie 2:")
print(movie2)
movie3=input("Enter fav movie 3:")
print(movie3)
list=[movie1,movie2,movie3]
print(list)

tup=(87,64,33,95,76,33)
print(type(tup))
print(tup[1])
# tup[2]=75. #this will give error
print(tup.count(33))

print(tup.index(33))

print(tup[2:3])
print(tup[:3]) #slicing works in same way as lists and strings

#WAP to check if a list contains a palindrome (same even after reversing) of elements
list1=[3,7,5,9,5,7,3]
list2=[2,4,'Gaurav',8]
print(type(list1))
print(type(list2))
list1_p=list1[::-1]
print(list1_p)
if list1==list1_p:
    print('Palindrome')
else:
    print('Non Palindrome')
#using copy and reverse method
list1=[3,7,5,9,5,7,3]
list1_p2=list1.copy() #we need to first create a copy and then use reverse method. If we use reverse method directly, the original list1 loses its order
list1_p2.reverse()
print(list1_p2)
if list1==list1_p2:
    print('Palindrome')
else: 
    print('Non Palindrome')


list2=['a','b','d','n','a','c']
list2.sort()
print(list2)

list2=['a','b','d','n','a','c']

print(list2.sort()) #This will give a non as sort method is used only does sorting and does not give any output.

print(list2.count('a')) #Gives count of a in the list

