"""
    https://codingdojang.com/scode/421
    지뢰찾기
    Lv. 3
    
    202010414
    (보고 따라 함 --> 아직 이해 못함)
"""

import random

m, n = map(int, input("Enter M, N: ").split(","))
print("m",m)
print("n",n)
#minelist = ["*","."]

mn = [[random.choice(['.','.','.','.','*']) for x in range(n)] for y in range(m)]
for y in mn:
    print(''.join(y))
r = mn.copy()
for y, yd in enumerate(r):
    for x, xd in enumerate(yd):
        if r[y][x] == '*': continue
        count = 0
        c = [[''] if y - 1 < 0 else r[y-1][0 if x - 1 < 0 else x - 1:x+2],
             r[y][0 if x - 1 < 0 else x - 1:x+2],             
             [''] if y + 1 >= m else r[y+1][0 if x - 1 < 0 else x - 1:x+2]]
        for z in c:
            count+=z.count('*')
        r[y][x] = str(count)

print("output")
for y in r:
    print(''.join(y))  

"""    
mn = []
for x in range(m):
    tmp = []
    for y in range(n):
        tmp += random.choice(minelist)
    mn += tmp

print("mn", mn)
"""

"""
q = []
for _ in range(m):
    q.append(list(input()))

for i in range(m): # 1
    for j in range(n): # 1
        if q[i][j] == '*':
            print('*', end='')
        else:
            count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0<=i+x<=m-1 and 0<=j+y<=n-1 and q[i+x][j+y] == '*':
                        count += 1
            print(count, end='')
    print()
"""