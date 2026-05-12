#Strings 
'''
it is a sequence of character.
'''
str1 = "this is a string"
str2 = 'Anubhav'
str3 = """this is a string"""

#why we need 3 different method to create string 
'''
when we need '' in string 
then
 '''
str1 = " hi my name is 'Anubhav ' ." #we can use '' in between string.
print(str1)

#if we need multiple line in string then what we do is 
'''
we use escape sequence character 
they gave formatting 
'''
str1 = "this is a \t string \n we are working in python ."
print(str1)

#string operations

a = "hello"
b = "world"
print(a+b) #concatination

print(len(str1)) #we can use length function to calculate length of string 
c = a + " " + b
print(len(a),len(b),len(c))

#indexing
str = "Anubhav"
print(str[0],str[1],str[2],str[3],str[4],str[5],str[6])

#slicing
'''
str[strting_index:ending_index:jumpping_length]
strating_index is included but ending_index is not .
'''
print(str[0:len(str)])
#negative indexing
print(str[::-1])
print(str[-3:-1])

#string function

str = "I am a coder."

str.endswith("er.") #returns true if string ends with substr

str.capitalize() #capitalize 1st char

str.title() #capitalize whole string

str.find("word") #returns 1st index of 1st occurence

str.replace("coder","doctor") #replace all occurence of old with new

str.count("am") #count the occurence of substr in string

print(str.endswith("er."))
print(str.capitalize())
print(str.title())
print(str.find("coder"))
print(str.replace("coder","doctor"))
print(str.count("am"))

#str = input("What is youyr name?")
#print(len(str))

#Conditional Statement 

'''
if(condition):
    Statement1
elif(condition):
    Statement2
else(condition):
    Statement3
'''

light = "green"

if(light == "red"):
    print("stop") #indentation
elif(light == "green"): #we can use multiple number of time elif 
    print("go")
elif(light == "yellow"): #if and else use only once in startin and in end of conditional statement .
    print("look")

#grade = int(input())
grade = 89 #for now ...
if (grade>=90):
    print("grade is A")
elif (90>grade>=80):
    print("grade uis B")
elif (80>grade>=70):
    print("grade is C")
else:
    print("you are fail")

#Nesting
'''
writing conditional statement inside in conditional statement 
'''

age = 2

if (age>= 18):
    if (age>=80):
        print("cannot drive")
    else :
        print("can drive")
else:
    print("cannot drive")

#WAP to check if a number entered by the user is odd or even .
'''
num = int(input("Enter the number ."))

if (num%2==0):
    print("number is even")
else:
    print("number is odd.")
'''

#WAP to find the greatest of 3 number entered by the use.

'''
num1 = int(input("Enter the number."))
num2 = int(input("Enter the number."))
num3 = int(input("Enter the number."))

if (num1>num2 and num1>num3):
    print(f"{num1} is greatest number")
elif(num2>num3 and num2>num1):
    print(f"{num2} is greatest number")
elif(num3>num1 and num3>num2):
    print(f"{num3} is greatest number")
else:
    print("invalid numbers")
'''

#WAP to check wheather the number is multiple by 7 or not .

'''
num = int(input("Enter the number ."))
if(num%7==0):
    print("number is multiple of 7")
else:
    print("number is not mulltiple of 7.")
'''

