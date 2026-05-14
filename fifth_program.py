#Loops
'''
loops are used to repeat instruction.
'''

#while loops
string = "hello" #we need to print this multiple times.
i = 10 #iterator
while(i>0):
    print(string,i)
    i = i-1 
'''
while condition:
    #some works
'''
'''
some practise question for while loop
'''


#print number from 1 to 100
count = 1
while(count<=100):
    print(count)
    count += 1


#print the multiplication table of a number n.
n = 23
i = 1
while(i<=10):
    print(n*i)
    i+=1

#print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100].
i = 1
while(i<=10):
    print(i*i)
    i+=1


#Search for a number x in this using loop .
tup = [1,4,9,16,25,36,49,64,81,100]
x = 9
i = 0
while(i<len(tup)):
    if tup[i]==x:
        print(f"we found out {x} in tup it is in {i+1}th position")
        break
    i+=1

#Break AND Continue
'''
Break : used to terminatethe loop when encountered
Continue : terminate execution in the current iteration & continues execution of the loop eith the next iteration 
'''

i = 1
while i<=5:
    print(i)
    if i ==3:
        break #it will break the loop .
    i+=1

i = 1
while i<=5:
    if i ==3:
        i+=1
        continue #it will by pass the iteration at i = 3 
    print(i)
    i+=1

i = 0
while(i<=10):
    if(i%2!=0):
        i+=1
        continue#by pass all odd values 
    print(i)
    i+=1

#For loop 
'''
loops are used for sequential transversal .for transvering ,list,string,tuple etc.
for loop
for el in list:
    #some work

for loop with else
for el in list:
    #some work
else:
    #work when loop ends
'''

list = [1,2,3,4,5]

for el in list:
    print(el)


for el in list:
    print(el)
else:
    print("End")

veggies = ["potata","tomato","lady finger","brinjal"]

for i in veggies:
    print(i)

tup = (3,1,5,2,65,3,6,2,8,21)

for i in (tup):
    print(i)

str = "anubhav"
for i in str:
    if(i=="h"):
        print("h found")
        break
    print(i)
else:#optional else.
    print(".")

'''
search for a number x in this tuple
'''
nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
for el in nums: #Linear search
    if (el == x):
        print(f"{x}  found.")
        break
else:
    print("END")

#range
'''
Range function returns a sequence of number , starting from 0 by default , and increase by 1 (by default),and stop before a specified number
range(start?,stop,step?)
'''
for el in range(5):
    print(el)
for el in range(1,5):
    print(el)
for el in range(1,5 ,2):
    print(el)

'''Practise question using for and range()'''

#Print number from 1 to 100
for i in range(1,101,1):
    print(i)
#Print number from 100 to 1:
for i in range(100,0,-1):
    print(i)
#Print the multiplication table of a number n.
n = 8
for i in range(1,11):
    print(n*i)

#WAP TO FIND THE SUM OF A FIRST N NUMBERS.(USING WHILE)

'''
n = int(input("Enter the natural number."))
sum = 0
while(n>0):
    sum += n
    n-=1
print(f"sum of first {n} natural number is {sum}")
'''

#WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS (USING FOR).

'''
n = int(input("Enter the natural number."))
product = 1
for i in range(1,n+1):
    product = product*i
print(f"factorial of {n} natural is {product}.")
'''