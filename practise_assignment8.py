'''Given a list of strings, check if all strings follow the format where the same word is repeated exactly twice with a hyphen in between them. The word repeated should not be empty. Examples of correct format:

 
 
"fast-fast" correct
 
"go-go" correct
 
"yeah-yeah" correct
 
 
Examples of incorrect format:

 
 
"fast-slow" incorrect (different words)
 
"fast-fast-fast" incorrect (word repeated more than twice)
 
"asfdadf" incorrect (no hyphen, word not repeated)
 
"fastfast" incorrect (no hyphen) "-" incorrect (empty word)
'''
def check_word(word):
    result = True
    num = len(word)//2
    if word[num]!= "-":
        result = False
    if word[0:num] != word[num+1::]:
        result = False
    if(result):
        print(f"The {word} follow the required format .")
  
word = input("enter the word which is appropriate according to given rules .")
while(word == ""):
    word = input("enter the word which is appropriate according to given rules .")
check_word(word)

'''
More efficient way of doing this 
def check_word(word):
    # 1. Split the string by the hyphen
    parts = word.split("-")
    
    # 2. To be correct, there must be EXACTLY 2 parts, 
    # they must be identical, and they must not be empty strings.
    if len(parts) == 2 and parts[0] == parts[1] and parts[0] != "":
        print(f"The '{word}' follows the required format.")
        return True
    else:
        print(f"The '{word}' does NOT follow the required format.")
        return False

word = input("Enter the word: ")
check_word(word)
'''