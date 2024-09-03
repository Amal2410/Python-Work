f=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\FileOperations\\news.txt","r")

# word_list=[]

# for line in f:

#     words=line.rstrip("\n").split(" ")

#     for w in words:

#         word_list.append(w)

# print(word_list)

word_list=[w for line in f for w in line.rstrip("\n").split(" ")]

# word_count={w:word_list.count(w) for w in word_list}

# print(word_count)

# wc={}

# for w in word_list:

#     if w in wc:

#         wc[w]+=1

#     else:

#         wc[w]=1

# print(wc)

wc={w:word_list.count(w) for w in word_list}

print(wc)

srt=sorted(wc,key=lambda key:wc.get(key),reverse=True)

print(srt)