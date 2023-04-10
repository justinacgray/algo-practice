import string
import re
alph = list(string.ascii_lowercase)
# test = ''

def word_score(word):
    score=0
    word = word.lower()
    check_alph =re.findall(r'[a-z]', word)
    word_check = check_alph
    print(type(word_check)) #list
    for i in range(len(word_check)):
        print('letter -->', word_check[i])
        for j in range(0,len(alph)):
            if word_check[i] == alph[j]:
                print(j+1, alph[j])
                x = j+1
                print("---->", x)
                score += x
    return f" Score is ==> {score}"



print(word_score('abcd545j#'))