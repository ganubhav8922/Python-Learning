#Basic Code
print("hello world")
print("Anubhav")
#print is a in-built Function 
#python has different variety character set .
print("My name is Anubhav" ,"My age is 18")
print("My name is Anubhav","\n","My age is 18")
print(23)
print(14+17,19-3,12*3,2//1,14/8)

#Variable 
#It is name given to a memory location in a program.

name = "Anubhav" #name is variable which store the value here value is Anubhav
age = 18 #here age is varibale 
print(f"my name is {name} and my age is {age}")
#variable is basically giving name to a memory location
age = 19 #now i changed variable value which is allowed
print(f"my name is {name} and my age is {age}")
#different type of variable available in python . in this case name is string variable and age is integer variable .
print("my name is ",name) #we can use different way to print variable .

#'=' is assigning operators which assigns the right value to left unlike equal of maths.
age1 = 19
age2 = 15
age2 = age1
print(age1,age2) #age1 value is assign to age2 as well by assigning operators.

#type is in-built function which gives type of variable.
print(type(name))
print(type(age))

#primarily ther3 is 5 data type 1 integer,2 string ,3 float ,4 boolean ,5 none .

a =  10 #integer
b = 'abhi'
c = "abhi"
d = '''abhi'''
# b,c,d all are string with different way of representation.
e = 10.00 # e is float
f = True #f is boolean 
g = None #g is none

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


#i can define few variable by some operation like sum.
a1 = 5
a2 = 10
sum = a1+a2
print(sum)

#comment = # ,
"""
jkshdkjahsdkjahsdkjahs
"""

#Operators
'''
1 ) Arithmetic (+,-,*,/,//,**,%)
2 ) Relational or comaprison(>,<,==,=<,=>,!=)
3 ) Logical(not,and ,or)
4 ) Assignment(=,+=,-=)'''

#arithmetic
b4 = 7
a4 = 9
sum = b4 +a4
print(sum)
print(a4+b4,a4-b4,a4*b4,a4/b4,a4//b4,a4**b4,a4%b4)

#relational

print(a4==b4,a4>b4,a4<b4,a4!=b4) #gives boolean output

#assignment

num = 10
#num = num + 10
num += 10
print(num)

#logical (works on boolean)

a = True
b = False
print(not a , a and b , a or b )

#type conversion and type casting
''' 
type conversion happens automatically (implicit)
where as type casting happens manually 
'''
a , b = 1,4.265
sum  = a+b
print(sum) #automatically conversion of integer to float

a,b = 1,"2"
sum = a + int(b) #explicit conversion or type casting
print(sum) 
c = int(b)
print(type(c))

#Input in pyhton 

a = input("enter you name")
print(f" hii {a}" , type(a))

b = int(input("enter your age ")) #by default it take string value so we need to type casting to desired data type 
print("your age is " , b)

