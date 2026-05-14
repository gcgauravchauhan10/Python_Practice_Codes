# Dictionaries and sets in python - think of these as macro variables
#Dictionary in Python - Pairs of words and meanings
#Word>>acts as 'key', meaning >> value
#"key" :value
info = {
    "key":"value",
    "name":"apnacollege",
    "marks":94.4,
    "subjects":["English","Hindi","Maths"]
}

info["key"]="lock" #dictionaries are mutable. new value can be assigned to a key
print(info)
#add new key to the dict
info["Favourite Sport"]="Cricket" #these two steps indicate the dictionaries are mutable
print(info)

#null dict
null_dict={}
print(null_dict)
#Nested dictionaries - Make a value of a key as another key
info1={
    "Name":"Gaurav",
    "Marks":{"Physics":95,
             "Maths":98,
             "Economics":78,
             "Social Science":79}
}
print(info1["Name"])
print(info1["Marks"]["Physics"]) #nested dictionary
print(info1["Marks"]["Maths"]) #nested dictionary

#Dictionaries methods
print(list(info1.keys())) # list is used to print in list form
print(tuple(info1.keys())) #tuple is used to print in tuple form
print(info1.values())
#NOTE_ - We can store lists in dictionary and dictionaries in list

print(info1.items()) #returns all key value payers as tuple - within parenthesis
pairs=list(info1.items())
print(pairs[0]) # follows the 0,1,2,3,4 order. pairs function needs to be used with square brackets

info1.get("Name")
print(info1.get("Name")) #gives same value as print(info1["Name"])
print(info1.get("Name2")) #Gives no error if key is not present
print(info1["Name2"]) #Gives error if key is not present in the dictionary

#update method
new_dict={"city":"Delhi"} 
info1.update(new_dict) #another way of adding a new key pair to a dictionaary
print(info1)

#Sets in Python - Each item in the set must be unique and immutable
#List and dictionaries can't be stored within a set because those are mutable
a={2,5,3,2,5,7,9,8}
b={1,2,2,3,4,4,5}

print(a)
print(b)
print(type(a))

collection={1,2,3,1,2,4}
collection.add(5)
collection.remove(2)
# strng=['a','ba','d','c']
# strng[0]='z'
# strng.reverse
# print(strng)

print(collection)
print(type(collection))
print(collection)
print(len(collection))  #during length calculation also, it removes duplicate values
#Empty set
collection={} #This is empty dictionary syntax
collection=set()
print(type(collection))

#Set methods - set is mutable but the elements are are immutable so lists and dictionaries can't be added as element
collection.add(1)
collection.add(2)
collection.add(4)
print(collection)
collection.add([2,4,3,8]) #set must only contain hashable values so that hash value does not change
print(collection)

collection={2,3,5,1,6,7,9}
collection.add(8)
print(collection)
collection.clear()
print(collection)

collection1={"Hello","Myname","Patna", "New Delhi","Newyork"}
collection1.pop() #randomly pops one value
print(collection1)

collection1={"Hello","Myname","Patna", "New Delhi","Newyork"}
collection2={"Myname","Patna","Newyork","Mumbai","Goa"}
print(collection1.union(collection2))
print(collection1.intersection(collection2))

#PRACTICE QUESTIONS
# 1. Store the following word meanings in a python dictionary
dict1={"table":["a piece of furniture","list of facts & figures"], #can u list or tuple or set for multiple meanings
       "cat":"a small animal"} 
print(dict1)
print(dict1["table"])
print(dict1["cat"])

# 2. You are given a list of subjects for students. assume one classroom is required for 1 subject.
# how many classrooms are required for by all students
subjects={"python","java", "C++","python","javascript","java","python","java","C++","C"}
print(type(subjects))
print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary
# and add one by one. Use subject name as key and marks as value
dict1={}
print(type(dict1))
dict1["Matchs"]=79
dict1["English"]=91
dict1["Science"]=98
print(dict1)

#Figure out a way to store 9 and 9.0 as separate values in a set (you can take help of built in data types)
set1={("int":9),("float":9.0)}
print(type(set1))
# a=int(9)
# b=float(9.0)
# print(a,b)
# set1.add(a)
# set1.add(b)
print(set1)




