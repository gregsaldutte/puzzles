def abbreviate(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    word_result = ""
    # Note that we have to make sure that the first character is indeed in the alphabet
    # In the test, there are something like "Complementary metal-oxide semiconductor" - "CMOS"
    # "Something - I made up from thin air" - "SIMUFTA"
    # "The Road _Not_ Taken" - "TRNT"
    
    # So I just extract something from the word-count problem
    temp_word = []  # this is a list to store any alphabet or number
    # Go over each letter in sentence_lower 
    for i in range(len(words)):
        char = words[i].lower()
        if char in alphabet:
            temp_word.append(char)
        elif char=='\'' and 0<i<len(words)-1:
            if words[i-1] in alphabet and words[i+1] in alphabet:
                temp_word.append(char)
        else:
            word_key = ''.join(temp_word)
            temp_word = []
            if word_key!='':
                word_result += word_key[0].upper()
            
        # We have to join the last temp_word if the last character is a alphabet
        if i == len(words)-1 and temp_word!=[]:
            word_key = ''.join(temp_word)
            word_result += word_key[0].upper()
            
    return word_result
    

