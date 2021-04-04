"""
    https://wikidocs.net/17114
    Q5 피보나치 함수
"""

""" my first trial
num = int(input("Enter number: "))

result = 0
arr = [0, 1]
while result <= num:
    if num<=2:
        break
    i = len(arr)
    result = arr[i-1] + arr[i-2]
    if result <= num :
        arr.extend([result])

print(arr)
"""


# answer
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

#for i in range(10):
#    print(fib(i))

num = int(input("Enter number: "))
i = 0
r = 0
arr = []
while r <= num:
    r = fib(i)
    arr.extend([r])
    print(i)
    i += 1

print(arr)

