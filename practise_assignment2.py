# Sample inputs 
a = int(input("Enter the number ."))

print(a>5)# bool: True if a greater than or equal to 5

print(a%5==0)# bool: True if a is divisible by 5

print(a%2!=0 and a<10)# bool: True if a is odd number less than 10

print(a%2!= 0 and -10<=a<=10)# bool: True if a is an odd number within the range -10 and 10

print(len(str(a))%2 == 0 and len(str(a))<10)# bool: True if a has even number of digits but not more than 10 digits


price1 = int(input("what is the price of good for offer 1."))
discount1 = int(input("what is the discount for the offer  1.")) # for offer1

price2 = int(input("what is the price of good for offer 1."))
discount2 = int(input("what is the discount for the offer  2."))# for offer2

# Assume discount is given in percentages

offer1 = price1*(1 - discount1/100)
offer2 = price2*(1 - discount2/100)

print(offer1<offer2)# bool: True if the offer1 is strictly cheaper
