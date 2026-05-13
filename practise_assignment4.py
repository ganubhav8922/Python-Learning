# Sample inputs 
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1+" "+word2# str: join word1 and word2 with space in between
print(output1)

output2 = word1[0:4]+"-"+word2[-4::]# str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between
print(output2)

output3 = word3+" "+str(n1)# str: join the word3 and n1 with a space in between
print(output3)

output4 = "-"# str: just the hypen "-" repeated 50 times
print(50*output4)

print(n2*output4)# str: just the hypen "-" repeated n2 times

output5 = str(n1)# str: repeat the number n1, n2 times
print(n2*output5)

print(word1==word2==word3)# bool: True if all three words are equal


print(word1<word2<word3)# bool: True if word1 comes before word2 and word3 assume all words are different


print("h" in word1)# bool: True if word1 has the letter h


print(word1.lower().endswith("a"))# bool: True if word1 ends with letter a or A


print("python" in sentence)# bool: True if the sentence has the word python
