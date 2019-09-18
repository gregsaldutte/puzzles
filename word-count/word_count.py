def count_words(sentence):
    word_count_dict = {}

    sentence_lower = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    
    temp_word = []  # this is a list to store any alphabet or number
    # Go over each letter in sentence_lower 
    for i in range(len(sentence_lower)):
        char = sentence_lower[i]
        if char in alphabet or char in number:
            temp_word.append(char)
        elif char=='\'' and 0<i<len(sentence_lower)-1:
            if sentence_lower[i-1] in alphabet and sentence_lower[i+1] in alphabet:
                temp_word.append(char)
        else:
            word_key = ''.join(temp_word)
            temp_word = []
            if word_key not in word_count_dict:
                word_count_dict[word_key] = 1
            else:
                word_count_dict[word_key] += 1
        # We have to join the last temp_word if the last character is a alphabet
        if i == len(sentence_lower)-1:
            word_key = ''.join(temp_word)
            if word_key not in word_count_dict:
                word_count_dict[word_key] = 1
            else:
                word_count_dict[word_key] += 1
    
    if '' in word_count_dict:
        word_count_dict.pop('')
    return word_count_dict


    
