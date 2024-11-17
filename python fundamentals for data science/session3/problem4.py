# print all palindromes
# need to remove the new line character at the end of every word 
import time

file_obj=open(r"python fundamentals for data science\session3\data\sowpods.txt")
words=file_obj.readlines()

tic=time.time()

for word in words:
    word=word.strip()
    if word==word[::-1]:
        print(word)
        
print(time.time()-tic)