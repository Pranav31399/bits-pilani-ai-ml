# print all word that contains all the vowels

import time

file_obj=open(r"python fundamentals for data science\session3\data\sowpods.txt")
words=file_obj.readlines()

tic=time.time()

for word in words:
    flag=True
    for vowel in 'AEIOU':
        if vowel not in word:
            flag=False
            break
    if flag==True:
        print(word)
        

# for word in words:
#     if 'A' in word and 'E' in word and 'I' in word and 'O' in word and 'U' in word:
#         print(word)

print(time.time()-tic)