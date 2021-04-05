"""
    https://codingdojang.com/scode/365
    generator
    d(91) = 9 + 1 + 91 = 101
"""


def generator(n):
    r = 0
    for i in str(n):
        r = r + int(i)
    return r + n
#print(generator(91))

arr = list(range(1, 5000))
for i in range(1,5000):
    if arr.count(generator(i)):
        arr.remove(generator(i))

print(sum(arr))

"""
def d_fn(n):
    y = n
    while n > 0:
        y += n % 10
        n //= 10
    return y

Z = [d_fn(n) for n in range(5000)]
print(Z)
A = [n for n in range(5000) if n not in Z]
print (sum(A))   
"""