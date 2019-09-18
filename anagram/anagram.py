def find_anagrams(word, candidates):
    cand_list = []
    word_list = list(word.lower())
    for cand in candidates:
        cand_temp_list = list(cand.lower())
        # The anagram should be of the same letter, and each letter appears for the same time, and could not be itself
        # Case insensitive
        for letter in word_list:
            if letter in cand_temp_list:
                cand_temp_list.remove(letter)
            else:
                break
        
        if cand_temp_list==[] and word.lower()!=cand.lower():
            cand_list.append(cand)
    
    return cand_list

