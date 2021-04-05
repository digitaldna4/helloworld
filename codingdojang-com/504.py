"""
    https://codingdojang.com/scode/504
    1~1000에서 각 수자의 개수 구하기
"""

arr = {i:0 for i in range(0,10)}
print("arr", arr)
for num in range(1,1001):
    s = str(num)
    for a in s:
        #print("a",a)
        arr[int(a)] += 1

print("arr", arr)