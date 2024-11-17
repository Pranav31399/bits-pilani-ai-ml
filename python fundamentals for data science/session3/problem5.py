# find the longest palindrome

import time

file_obj=open(r"python fundamentals for data science\session3\data\sowpods.txt")
words=file_obj.readlines()

tic=time.time()
longest=''
for word in words:
    word=word.strip()
    if word==word[::-1]:
        if len(longest)<len(word):
            longest=word
        
print(longest)
print(time.time()-tic)