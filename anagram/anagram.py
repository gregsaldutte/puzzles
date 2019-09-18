def find_anagrams(word, candidates):
    cand_list = []
    for cand in candidates:
        cand_compare = cand.lower()
        # The anagram should be of the same letter, and each letter appears for the same time, and could not be itself
        # Case insensitive
        for letter in word.lower():
            if letter in cand_compare:
                cand_compare.remove(letter)
        
        
        if cand_compare=='':
            cand_list.append(cand)
    
    return cand_list

print(find_anagrams('mass',['last']))