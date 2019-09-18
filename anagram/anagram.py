def find_anagrams(word, candidates):
    cand_list = []
    word_list = list(word.lower())
    word_list = word_list.sort()
    print(word_list)
    for cand in candidates:
        cand_list_temp = list(cand.lower())
        cand_list_temp = cand_list_temp.sort()
        print(cand_list_temp)
        # The anagram should be of the same letter, and each letter appears for the same time, and could not be itself
        # Case insensitive
        if cand_list_temp==word_list and len(word)==len(cand) and word.lower()!=cand.lower():
            cand_list.append(cand)
    
    return cand_list

print(find_anagrams('mass',['last']))