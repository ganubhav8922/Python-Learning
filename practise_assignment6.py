#part 1

x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`
x1,x2=x2,x1

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 
y1,y2,y3=y2,y3,y1

# create a new variable `a` with the value of `z`
a = z

# delete the variable `z`
del z
print(x1,x2,y1,y2,y3)



#part 2

# A single quote ' and a double quote "
output1 = "A single quote \' and a double quote \""

# A forward slash / and a backward slash \
output2 = "A forward slash / and a backward slash \\"

# Three single quotes ''' and three double quotes """
output3 = "Three single quotes ''' and three double quotes \"\"\""

# Double forward slash // and Double backward slash \\
output4 = "Double forward slash // and Double backward slash \\\\"

print(output1,output2,output3,output4)




