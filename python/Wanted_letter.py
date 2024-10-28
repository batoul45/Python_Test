def most_wanted_letter(text):
    # First of all we need to Convert all characters to lowercase 
    text = text.lower()
    
    # Now we need to  keeps track of each letter we find in the input and how often it appears
    # So basicly every letter becomes a key , and its "value" is the count of that letter
    
    letter_list = {}
    
    # Next step is to count  occurrences of every letter in the text we have
    for letter in text:
        # It is necessery to verify if the character is a letter 
        if 'a' <= letter <= 'z' or 'à' <= letter <= 'ÿ':
            if letter in letter_list:
                letter_list[letter] += 1
            else:
                letter_list[letter] = 1
    
    # If we dont find any letters ,just  return a warning message
    if not letter_list:
        return "No letters Found"
    
    # Find the letter with the highest frequency. In case of a tie, return the lexicographically first letter.
    most_common_letter = None
    max_occur = 0
    
    for letter, count in letter_list.items():
        if count > max_occur  or (count == max_occur  and (most_common_letter is None or letter < most_common_letter)):
            most_common_letter = letter
            mmax_occur  = count
    
    return f"The most wanted letter is '{most_common_letter}'"

#lets give it try
print(most_wanted_letter("Hello World!"))          
print(most_wanted_letter(""))                      
