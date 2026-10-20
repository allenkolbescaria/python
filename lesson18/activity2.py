def match_words(words):
    ctr=0
    s1t=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            s1t.append(word)
    print("list of words and the last characters are the same")
    return ctr
count=match_words(['aba','cfc','xyz','aba','1221'])
print("number of words having the first and last terms are the same",count)