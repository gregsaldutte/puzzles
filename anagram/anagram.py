def find_anagrams(word, candidates):
    cand_list = []
    word_list = list(word.lower()).sort()
    for cand in candidates:
        cand_list = list(cand.lower()).sort()
        # The anagram should be of the same letter, and each letter appears for the same time, and could not be itself
        # Case insensitive
        if cand_list==word_list and len(word)==len(cand) and word.lower()!=cand.lower():
            cand_list.append(cand)
    
    return cand_list

