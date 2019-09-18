def is_isogram(string):
    list = []
    for n in string:
        list.append(n)
    unique_list = set(list)
    if(len(unique_list) == len(list)):
        print("The word " + string + " is an isogram!")
    else:
        print("The word " + string + " is not an isogram!")

is_isogram("Jack")
