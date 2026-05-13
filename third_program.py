#Lists
'''
A built in data that stores set of value 
it is kind of array of python .
it can store element of different data type unlike array of c .
'''

marks = [10,89,96,56,98,45.94] #marks is a list .
print(marks[2]) #it allows indexing .

student1 = ["Anubhav",25048,99,"Kanpur"]

print(student1)
'''
String is immutable but 
list is mutable (can change)
'''
student1[2] = 98

print(student1)

print(student1[0:3]) # it also support slicing.

#List methods 
'''
some function which used specefically for list .
list.append() #it appends that element to the last in the list
list.sort() #it sorts the list 
list.sort(reverse=True) 
list.reverse() #reverses list
list.inser(idx,ele) #insert element at index
list.remove() #remove first occurence of elemnt 
list.pop(idx) #remove element at idx
'''

#list.append()
l = [1,2,3]
l.append(4)
print(l)

#list.sort()
#ascending
l = [3.12,6,2,0,45,92,16]
print(l.sort()) #it returns the None value.
print(l) #now it automatically sort .
#descending
l.sort(reverse=True)
print(l)
#we can use sorting to different data type as well .
list = ["banana" ,"apple" ,"leeche" ,"mango" ,"guavava"]
list.sort() #by alphabetical order 
print(list)
list.sort(reverse = True)
print(list)

#list.reverse()
l = ['a','b','c','g','t']
l.reverse()
print(l)

#list.inser(idx,ele)
l = ['a','b','c','g','t']
l.insert(1,'d')
print(l)

#list.remove() & list.pop(idx)
l = ['a','b','c','g','t']
l.remove('a')
print(l)
l.pop(3)
print(l)


#Tuple
'''
it works very similar to tuple . 
the major difference is that it is immutable (just like string)
tuple = (2,8,0,8)
'''

tuple = (3,9,5,0,3)
print(type(tuple))
print(tuple[3]) #indexing is allowed .
#tuple[2] = 5 assigning is not allowed .

tup = (1,2,3,4,5,6,7,8) #for single element we need to seperate by comma . if we do not put comma then python take it as a integer or float or any other data type other that tuple .
print(tup , type(tup))
print(tup[1:5]) #slicing is allowed

#tuple methods 
'''
tup.index() #return index of first occurence
tup.count() #counts total occurence 
'''

#tup.index()
tup = (1,2,3,4,5,6,7,8)
print(tup.index(4))

#tup.count()
tup = (1,2,3,4,5,6,7,8)
print(tup.count(3))


#WAP to ask the user to enter names of their 3 favorite movie & store then in a list.
'''list = []
i=0
while (i<3):
    a = str(input("Enter the name of your favourite movie ."))
    list.append(a)
    i = i+1

print(list)
'''

#WAP to check if a list contains a palindrome of elements .
'''
list = []
i = int(input("How many elements you want in list."))
while(i>0):
    a = (input("enter the element in the list ."))
    list.append(a)
    i = i-1

list1 = list.copy()
list1.reverse()
flag = True
for i in range(len(list)):
    if (list[i] != list1[i]):
        flag = False

if(flag):
    print("yes it is pallindrome")
else:
    print("no is not pallindrome")
     
'''
