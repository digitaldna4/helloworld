"""
    https://codingdojang.com/scode/634
    텍스트가 입력으로 주어질때 단어의 개수를 세는 프로그램
    << 미완성 >>
"""

filenm = "634.txt"

f = open(filenm,'r')
readlns = f.readlines()
f.close

print(readlns)
words = []
for readln in readlns:
    readln.replace(',',' ').replace('.', ' ')
    words.append(readln.split(' '))
print(words)    

<< 미완성 >>
