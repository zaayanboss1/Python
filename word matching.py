def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("List of words with first and last character same/n")
    return ctr
count=match_words(['abc','cfc','xyz','aba','1221'])
print("Number of words having first ans=d last character same:",count)