#Function
'''
block of statements that perform a specific task .
'''

'''
def func_name(param1,param2...): #function definition
    #some work
    return val

    
    
func_name(arg1,arg2 ..) #function call
'''

def sum(a,b): #defining of the function
    s = a+b
    return s

num = sum(34,876) #calling the function.
print(num)

#function helps us to redundant code .
#parameter and return is optional

def print_hello():
    print("hello")

print_hello()


#Function in pyhton is of two types .
'''
1 ) Built -in function [print(),len(),type(),range()]
2 ) User defined Function 
'''

print("hello",end=" ") #sep = " "
print("world") #emds = "\n"

#user defined function are those function which are defined by user/programmer .

def cal_prod(a=1,b=1): #we can use default value so that it is not necessary to fill complete parameter . non default value follows default value.
    print(a*b)
    return a*b

cal_prod(2)


#lets practise

'''
WAP to print the length of a list


def len_list(a):
    print(len(a))
a = []
ch = 0
while(ch!=""):
    ch = input("enter the element in list")
    if ch == "":
        break
    a.append(ch)

len_list(a)

'''

'''
WAP to print the element of a list in a single line (list is the parameter)

def list_element_print(a):
    for i in range(len(a)):
        print(a[i])


a = []
ch = 0
while(ch!=""):
    ch = input("enter the element in list")
    if ch == "":
        break
    a.append(ch)
list_element_print(a)

'''

'''
WAP to find factorial of n 


def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("enter the number ."))
fac = factorial(n)
print(f"factorial of {n} is {fac}.")

'''

'''
WAP to convert USD TO INR


def usd_to_inr(num,exchange_rate):
     return num*exchange_rate

num = int(input("how many usd you have."))
exchange_rate = int(input("1 $ is equal to how many ₹."))
temp = usd_to_inr(num,exchange_rate)
print(f"value of {num}$ in ₹ is {temp}.")
'''


#Recursion
'''
when a function calls itself repeatedly
'''

#print n to 1 backward
def show(n):
    if n==0: #base case .
        return
    print(n)
    show(n-1)

n = 10
show(n)
#loops and recursion are interconnected.


def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
    
temp = factorial(11)
print(temp)

#lets practise

'''
write a recursive function to calculate the sum of the first n natural numbers.


def natural_sum(n):
    if n == 0:
        return 0
    return n + natural_sum(n-1)

temp = natural_sum(10)
print(temp)

'''
