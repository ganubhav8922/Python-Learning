"""
    Returns the letter which occurs most frequently as the first letter of any word (case insensitive).

    Args:
    passage (str): A multi-line string representing the passage.

    Returns:
    str: The most frequently occurring first letter in lowercase.
    """

def most_occurring_first_letter(passage: str) -> str:
    words = passage.split()
    words_dict = {} 
    
    for i in range(len(words)):
        # Safety check: ensure the word isn't empty (e.g. random punctuation or spaces)
        if len(words[i]) == 0:
            continue
            
        # Move .lower() HERE so the function is truly case-insensitive on its own
        first_letter = words[i][0].lower()
        
        if first_letter not in words_dict:
            words_dict[first_letter] = 1
        else :
            words_dict[first_letter] += 1
            
    max_count = 0 
    best_letter = ""
    for letter, count in words_dict.items():
        if count > max_count:
            max_count = count
            best_letter = letter
            
    print(f"The most occurring first letter is '{best_letter}' with a count of {max_count}")
    return best_letter


# --- Input Loop ---
# Since .lower() is now inside the function, you don't even need it here!
num = input("Enter your words one by one. Enter a single period '.' to stop: ")
passage = num + " "
while (num != "."):
    num = input("Enter your words one by one. Enter a single period '.' to stop: ")
    if num == "." :
        break
    else :
        passage += num + " "

most_occurring_first_letter(passage)