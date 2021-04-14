"""
    https://codingdojang.com/scode/421
    지뢰찾기
    Lv. 3
    
    202010414
    (완성 못함)
"""

m, n = map(int, input('Enter M, N: ').split())
print("m",m)
print("n",n)

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
