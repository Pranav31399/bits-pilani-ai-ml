# print all alphabets that never appear double like AA in the file sowpods.text
import time

alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

file_obj=open(r"python fundamentals for data science\session3\data\sowpods.txt")
words=file_obj.readlines()

tic=time.time()
for alpha in alphabets:
    flag=True
    for word in words:
        if alpha*2 in word:
            flag=False
            break
    if flag==True:
        print(alpha)
    
print(time.time()-tic)