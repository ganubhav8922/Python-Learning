# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = int(input("enter the number"))
b = int(input("enter the number"))
# <eoi>

print(a+b)# int: sum of a and b
print(2*(a+b))# int: twice the sum of a and b
print(abs(a-b))# int: absolute difference between a and b
print(abs((a+b) - (a*b)))# int: absolute difference between sum and product of a and b

original_price = int(input("what is the original price ."))
discount_percentage = float(input("What is the discount percentage ."))

# Find discounted price given price and discount_percent
discounted_price = original_price - (discount_percentage*(original_price/100))
print(f"discounted price is {discounted_price}")

# input variables : original_price: int, discount_percent: floa
# output : discounted_price:float

# Round the discounted_price
round_discounted_price = round(discounted_price)
 # int
print(f"round off value of discounted price {round_discounted_price}")


# Find hrs and mins given the total_mins
total_mins = int(input("give the value of total minutes ."))

hours = total_mins//60
mins = total_mins%60

print(f"total hours is {hours} and minutes is {mins}")



# input variables : total_mins
# int: hint: think about floor division operator
# int
