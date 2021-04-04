"""
    https://wikidocs.net/17114
    Q6 숫자의 총합 구하기
"""

str = input("Enter multiple numbers seperated by comma(',')\n")
sum = 0
for s in str.split(","):
    n = int(s)
    sum = sum + n

print(sum)
