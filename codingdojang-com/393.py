"""
    https://codingdojang.com/scode/393
    1~10000에서 8이라는 숫자가 총 몇번 나오는가?
"""

cnt = 0
arrEight = []
for i in range (1, 10001):
    for n in str(i):
        if n=="8":
            cnt += 1
            arrEight.extend([i])

print("cnt",cnt)
print("arrEight",arrEight)

# str(list(range(1, 10001))).count('8')