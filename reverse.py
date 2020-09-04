def string_Reverse(string1):
    stringFinal = ''
    index = len(string1)
    while index >0:
        stringFinal += string1[index -1]
        index = index -1
    return  stringFinal
print(string_Reverse('1234abcd'))