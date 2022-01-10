#BOJ 1157

#TIL: Pick up unique alphabet -> Use dictionary. -> To string: "".join(dict.fromkeys(string))

word = input()
tstWord = word.lower()

if len(word) == 1:
    print(word.upper())

else:
    uniqueAlph = "".join(dict.fromkeys(tstWord))
    cnt = 0
    cntlist = []
    for i in uniqueAlph:
        cnt = tstWord.count(i)
        cntlist.append(cnt)
    if cntlist.count(max(cntlist)) != 1:
        print ("?")
    else:
        print(uniqueAlph[cntlist.index(max(cntlist))].upper())