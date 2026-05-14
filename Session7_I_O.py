#===================================================#
#=========File input and output in python===========#
#===================================================#
#Types of all files
# 1. Text files:.txt,.docx,.log etc.
# 2. Binary files : .mp4,.mov,.png., jpeg etc.

datafile=open ("/Users/gauravchauhan/Downloads/students.csv")
data=datafile.read()
print(data)

#Text file - stored in form of characters

datafile=open ("/Users/gauravchauhan/Downloads/students.csv","r") #To read only (This is default also, if dont specify)

data=datafile.read() #reads and print the 'entire data' with type of data
print(data)
datafile.close


#r - read
#w - open for writing, truncating the file first, writes from scratch
#x - create a new file and open it for writing
#a - open for writing, appending to the end of the file if it exists
#t - text mode
#b - binary mode
#+ - open a disk file for updating (reading and writing)

line1=datafile.readline() #reads one line at a time. Does not work right after read() as there is nothing left to read
print(line1)

datafile=open ("/Users/gauravchauhan/Downloads/students.csv","a") #open for writing

d=datafile.write("I want to learn JavaScript tomorrow")

print(d)

datafile1=open ("sample.txt","a") #open for writing. this step automatically creates a file if it does not exist, it will not write into it in first go though

datafile1.write("I want to learn JavaScript tomorrow")

datafile1.write("I am too busy today")

datafile2=open ("sample.txt","w") #open for writing
datafile2.write("I want to rock in Python coding and cant wait to accomplish it")
datafile2.close
datafile3=open ("sample.txt","w") #open for writing
datafile3.write("Upskill and kill") #Should overwrite the opened file
datafile3.write("I want to rock in Python coding and cant wait to accomplish it") #Should overwrite the opened file

datafile3=open ("sample.txt","a") #open for writing
datafile3.write("Upskill and kill") #Should overwrite the opened file
datafile3.write("\nI want to rock in Python coding and cant wait to accomplish it") #Should overwrite the opened file
datafile3.close

datafile4=open ("sample.txt","r+") #open for read+ no truncate
datafile4.write("Upskill and kill") #Should overwrite the opened file
datafile4.write("I want to rock in Python coding and cant wait to accomplish it") #Should overwrite the opened file
datafile4.close

datafile4=open ("sample.txt","a+") #open for append. no truncate
datafile4.write("Upskill and kill") #Should overwrite the opened file
datafile4.write("I want to rock in Python coding and cant wait to accomplish it") #Should overwrite the opened file
datafile4.close

with open("sample.txt","r") as f: #f is the alias like sql. data close is not required when using "with"
    data = f.read()
    print(data)

with open("sample.txt","w") as f: #f is the alias like sql. data close is not required when using "with"
    data = f.write("BJP won the Bengal election")
    print(data)

#Deleting a file
#cant delete the file with .delete, we need to use a module for that
import os
os.remove("practice.txt") #Removes file from the location

#Practice - create a txt file, write few lines and replace Java with Python in the file text
with open("practice.txt","a+") as df:
    data_=df.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    print(type(data_))

with open("practice.txt","r") as rf:
    dataread = rf.read()
    newdata = dataread.replace("Java","Python")
    print(newdata)
    
#now open the file in write mode
with open("practice.txt","w") as wf:
    datawrite = wf.write(newdata)

with open("practice.txt") as pt:
    i=1
    linecount=len(pt.readlines())
print(linecount)

#WAF to find in which line of file does the word "learning" occur first

with open("practice.txt") as pt:
    linelist=pt.readlines()
    print(linelist)
    linecount=len(linelist)
    print(linecount)
for i in range(0,linecount):
    found_flag = linelist[i].find("learning")
    if found_flag >=0:
        print(i+1)
        break
i +=1

#Now using enumerate
with open("practice.txt") as pt:
    linelist=pt.readlines()
    print(linelist)
    linecount=len(linelist)
    print(linecount)
for i,line in enumerate(linelist,start=0):
    if 'learning' in line:
        print(i+1)
        break
    i +=1

#Another method
def check_for_line(word):
    data = True
    line_no = 1
    with open("practice.txt","r") as pt:
        while data:
            data = pt.readline()
            if word in data:
                print(line_no)
                break
            line_no +=1
            
check_for_line("Python")

#Alternate method suggested by Python    
with open("practice.txt") as pt:
    lines = pt.readlines()

for i, line in enumerate(lines, 1):
    if 'learning' in line:
        print("Word 'learning' first found at line:", i)
        break

# From a file contatin numbers separated by comma, print the count of even numbers
with open("newfile.txt","+a") as nf:
    nf.write("1,2,4,6,8,9,11,15,17,19,51,52,54,100")

#without split method
with open("newfile.txt","r") as nfr:
    text=nfr.read()
    num=""
    even_cnt = 0
    #list = text.split()
    for i in range(len(text)):
        if text[i] ==",":
            if int(num)%2 == 0:
                even_cnt +=1
                num=""
        elif i == len(text)-1:
            num +=text[i]
            if int(num)%2 == 0:
                even_cnt +=1
        else:
            num +=text[i]    
print(even_cnt)

#with split method
with open("newfile.txt","r") as nfr:
    text=nfr.read()
    even_cnt = 0
    list = text.split(",")
    for val in list:
        if (int(val))%2 == 0:
                even_cnt +=1
print(even_cnt)

