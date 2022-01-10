#BOJ 10809

#TIL: To get lower alphabet in list -> string.ascii_lowercase

import string

word = input()

alph_lower = list(string.ascii_lowercase)
pos = 0
res = ""
for i in alph_lower:
    pos = word.find(i)
    res = res + str(pos) + " "
print (res.rstrip())