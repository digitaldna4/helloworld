"""
    https://wikidocs.net/17114
    Q4 리스트 총합 구하기
"""

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

"""
sum = 0
B = []
for a in A:
    if a>= 50:
        B.extend([a])
        sum += a
print("B:", B)
print("Sum:", sum)
"""

result = 0
B = []
while A:
    mark = A.pop()
    if mark >= 50:
        B.extend([mark])
        result += mark

print("B:", B)
print(result)