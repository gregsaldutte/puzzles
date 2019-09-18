def abbreviate(words):
    list = words.split(" ")
    word = ""
    for i in list:
        word = word + i[0]
    print(word)
    
abbreviate("This is a nice word")
