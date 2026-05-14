#Strings
Str1 = "This is a Gaurav's string. We are creating it in Python"   # String is a sequence of characters enclosed in single or double quotes
str2 = 'My company is Google'    # String can also be enclosed in single quotes
str3 = """I am "learning" Python""" # String can also be enclosed in triple quotes for multi-line strings

#Escape sequence characters
str4 = 'I am learning Python\nIt is very interesting' # \n is used for new line
str5 = 'I am learning Python\tIt is very interesting' # \t is used for tab space
str6 = 'I am learning Python\'s basics' # \' is used to include single quote in string
str7 = "I am learning Python\"s basics" # \" is used to include double quote in string

print(Str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)


print(Str1+str2)

print(len(Str1)) # len() is used to find the length of the string
final_str=str6+" " + str7    # String concatenation using + operator. We can also use f-string for concatenation. final_str = f"{str6} {str7}"
print(final_str)

#Indexing and slicing of strings
print(Str1[1]) # Indexing starts from 0. It will print the second character of the string
print(str2[3]) # It will print the fourth character of the string
char_4=str2[3]
print(char_4)

#Slicing
Str1_slice=Str1[1:15]
str2_slice=str2[3:5]
str3_slice=str3[3:] # It will print the string from index 3 to index 4. Index 5 is not included
str4_slice=str4[:10] # It will print the string from index 0 to index 9. Index 10 is not included

print(Str1_slice) # It will print the string from index 1 to the end of the string
print(str2_slice) # It will print the string from index 3 to index 4   
print(str3_slice) # It will print the string from index 3 to the end of the string
print(str4_slice) # It will print the string from index 0 to index 9

#Slicing using backward indexing
Str1_slice_back=Str1[-1] # It will print the last character of the string
str2_slice_back=str2[-3] # It will print the third last character of the string
str3_slice_back=str3[-5:] # It will print the last 5 characters of the string
str4_slice_back=str4[:-10] # It will print the string from the beginning to the minus tenth character of the string
print(Str1_slice_back) # It will print the last character of the string
print(str2_slice_back) # It will print the third last character of the string
print(str3_slice_back) # It will print the last 5 characters of the string
print(str4_slice_back) # It will print the string from the beginning to the third last
#conditional statements

#string functions
a="My name is Cha$uhan. I am $the $best"
b="If you are bad, I am your dad."
print(len(a))

print(a[:5])
print(a[1:5])
print(a[-7:])

#endswith
print(a.endswith("est"))
print(a.endswith("ese"))

#capitalize
print(a.capitalize())
str1=a.capitalize()
print(str1)
#replace function
str1=a.replace("best", "worst")
print(str1)
#Find
str1=a.find("best")
print(str1)
print(b.find("dad"))

#count
print(b.count("I"))

abc=input("Write your first name:")

print("Length of your name is",len(abc)) #Check this again..there is some issue here
print(a.count("$"))

#Conditional statements
#if elif else

a=50
b=19
c=30
if a>=50 and b<18:
    c=c+30
elif a>=50 and b==18:
    c=c+10
else:
    c=c+15
print(c)

n=5
if n<<5:
    ncount="Less Than 5"
elif n==5:
    ncount="Equals 5"
else:
    ncount="Greater Than 5"

print(ncount)

