# Sample inputs 

s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
# <eoi>

print(s[2])# str: get the third character of s

print(s[-4])# str: get the fourth last character of s

print(s[0:3])# str: get the first 3 characters of s

print(s[0::2])# str: get every second character of s

print(s[-3::])# str: get the last 3 characters of s

print(s[::-1])# str: get the reverse of s

a = int(course_code[3])
print(a)# int: get the term of the year as number from course_code
b = int(course_code[0:2])
print(b)# int: get the year as two digit number from course_code
