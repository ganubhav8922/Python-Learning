# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool



# <eoi>

# part 1 - basic if

new_word = word# donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word[-3::] == "ing":
    new_word = new_word[:-3:]

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here
if continuous_tense:
    new_word = new_word+"ing"



# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age <18:
    age_group = "Child"
else :
    age_group = "Adult"


# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if is_member:
    applicant_type = age_group+" Member"
else:
    applicant_type = age_group+" "+"Non-member"



    