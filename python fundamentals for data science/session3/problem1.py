# Find all the words which contains 'UU' in the word in the file sawpods.txt

# step1 : read the file and every time you open a file you should close it
file_obj=open(r"python fundamentals for data science\session3\data\sowpods.txt")
words=file_obj.readlines()

# result=[]
for word in words:
    if 'UU' in word:
        print(word)
        # result.append(word)

# print(len(result))
# print(result)
file_obj.close()