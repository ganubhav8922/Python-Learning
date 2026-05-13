input1 = int(input("Enter the age ."))# int: Read a number as integer from standard input
input2 = input("Enter the date month and year as ddmmyy .")
input3 = input2[0:2]+"/"+input2[2:4]+"/"+input2[4:6] # str: Read a string of format dd/mm/yy from standard input
input2a,input2b,input2c =int(input2[0:2]),int(input2[2:4]),int(input2[4:6]) # int, int, int: Get the correct parts from dob as int

fifth_birthday =input2[0:2]+"/"+input2[2:4]+"/"+str(input2c+5)
print(f"fifth birthday is on {fifth_birthday}")# str: fifth birthday formatted as day/month/year 

last_birthday = input2[0:2]+"/"+input2[2:4]+"/"+str(input2c+input1)
print(f"your last birthday was on {last_birthday}")# str: last birthday formatted as day/month/year


if(input2b>2):
    dob_after_10months = input2[0:2]+"/"+str(input2b+10-12)+"/"+str(input2c+1)
else:
    dob_after_10months = input2[0:2]+"/"+str(input2b+10)+"/"+str(input2c)
print(f"don after 10 month is {dob_after_10months}")# str: dob same day after 10 months formatted as day/month/year




weight = float(input("enter the weight as float ."))# float: Read a number as float from stdin(Standard input)

kgs = int(weight)
grams = (weight - kgs)*1000
# str: reformat weight of format 55 kg 250 grams

print(f"weight is {kgs} kg and {grams} gram ")# print weight_readable 
