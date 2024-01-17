def tokenizer(stri,deli):
    final = []
    i = 0
    while i<len(stri):
        word = ""
        while i<len(stri) and stri[i] != deli:
            word += stri[i]
            if(i<len(stri)):
                i += 1
        final.append(word)
        word = ""
        i+=1
    return final

print(tokenizer("hello every one"," "))
