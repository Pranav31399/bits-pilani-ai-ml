# find all the words that are present in sonnet_words.text but not in sowpods.txt

import time

file_obj1=open(r"python fundamentals for data science\session3\data\sonnet_words.txt")
sonnet_words=file_obj1.readlines()
sonnet_words=[word.strip() for word in sonnet_words] 

file_obj2=open(r"python fundamentals for data science\session3\data\sowpods.txt")
sowpods_words=file_obj2.readlines()
# cleaning the word and converting it into set, because searching in set and dict is very fast
sowpods_words={word.strip() for word in sowpods_words}

tic=time.time()

for sonnet in sonnet_words:
    if sonnet not in sowpods_words:
        print(sonnet)