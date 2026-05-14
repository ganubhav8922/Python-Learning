#Dictionaries
'''
they are used to store data value in key:values pairs
they are unordered , mutable(changeable) & don't allow duplicate keys
'''

dict ={
    "name":"Anubhav",
    "roll_no":25048,
    "marks":100,
    "subjects":["python","c","java"],
    "topics":["dictionary","set"]
}
#we can take any data type as a value in dictionary but we can not take list and dictionary as key .
print(type(dict))

#Properies of dictioanry 
'''
they are unordered
unlike list , tuple , string 
hence we cannot perform indexing
they are mutable which means we can change and we also cannot duplicate use key
'''

print(dict["name"]) # we can print values.
dict["name"] = "Abhinav" #we can change values
print(dict["name"]) 
dict["grade"] = "A"  #we can add new key and their respective values in dictionary
print(dict["grade"])

#i want to create null dictionary
null_dict = {}
print(null_dict)
null_dict["name"] = "Anubhav"
print(null_dict)

#Nested Dictionary
student = {
    "name" : "Anubhav",
    "subject":{
        "phy":100,
        "chem":100,
        "maths":100,
    }
}

print(student)
print(student["subject"])
print(student["subject"]["maths"])

#Dictionary Methods
'''
mydict.keys() #returns all keys.
mydict.values() #returns all values.
mydict.items() #return all(key,valu) pairs as tuple
mydict.gey #returns the key according to value
mydict.update(newDict) #insert the specified items to the dictionary
''' 

print(student.keys())
print(student.values())
print(list(student.keys()))
print(len(student))


print(student.items())
pairs = list(student.items())
print(pairs[0]) #we can call individual pair of key and value like this .


print(student.get("name2")) #it will give null 
#print(student["name2"]) #it will give error .program will not run after this .
'''
that the difference between normal and .get()
'''
print(student.get("name"))
print(student["name"])


student.update({"city":"delhi","age":16,"name":"ABHINAV"}) #we can add whole new dictionary to old one and also madofy value of old one 
print(student)


#Set 
'''
it is the collection of the unordered items .
each element in the set must be unique & immutable.
'''
null_set = set()
set1 = {1,2,2,2,2} #repeated elements stored only once , so ir resolved (1,2)
print(set1)

collection = {1,2,3,4,"hello",2,2,4,4,"hello"}
print(collection) #duplicate values will be ignored .
print(type(collection))
print(len(collection))#length also ignoed duplicate.

collection1 = {} #this is empty dictionary
collection = set() # this is syntax for creating empty dictionary.

#Set Methods
'''
set.add(element) #adds on elemenmts
set.remove(elements) #removes the elements
set.clear() #empties the set
set.pop() #removes the random value
'''

#set is mutable , but their elements are immutable .

collection = set()
collection.add(1)
collection.add(2)
collection.add("hdfgsdfhg")
collection.add((1,3,2,2,))#tuple is immutable so we can add into set.
#collection.add({"1":0,"2":2}) #dictionary is mutable so it can not add in to the set

collection.remove(1)

print(collection)

collection = {"hello","apnacollege","world","coding","python"}

print(collection.pop())
print(collection.pop())

"""
set.union(set2) #combines both set values &returns new.
set.intersection(set2) #combines the common values & return nre 
"""

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) #it dies not change set 1 
print(set1.intersection(set2))


"""
Store following word meaning in a python dictionary.
table : "a piece of furniture","list of facts & figures"
cat : "a small animal"
"""

'''
dict = {}
num = int(input("how many words you want to enter."))
for i in range(num):
    a = input("Enter the word:")
    temp = int(input("how many meaning you have for this word."))
    li = []
    for j in range(temp):
        meaning = input(f"enter the meaning of {a}")
        li.append(meaning)
    dict[a] = li
print(dict)
'''



'''
You are given a list of subjects . Assume one classroom is required for 1 subject. How many classroom are needed by all students.
'''

'''
li = set()
num = int(input("How many subjects are there."))
for i in range(num):
    sunject = input("enter the name of subjects.")
    li.add(sunject)

print(f"there will be {len(li)} number of classroom are required .")
'''