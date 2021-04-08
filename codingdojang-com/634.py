"""
    https://codingdojang.com/scode/634
    텍스트가 입력으로 주어질때 단어의 개수를 세는 프로그램
    << 미완성 >>
"""

filenm = "634.txt"

f = open(filenm,'r')
readlns = f.readlines()
f.close

#print(readlns)
words = []
for readln in readlns:
    print("readln", readln)
    tmp = readln.replace(',','').replace('.', '').replace('\n','').split(' ')
    print("tmp", tmp)
    words.extend(tmp)
print(words)    

dic = {}
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
#print(dic)
#print(dic.items())

lst = sorted(dic.items(), key=lambda k: k[1], reverse=True )
#print("----- lst\n",lst)
for w, c in lst[:10]:
    print(w,c)

