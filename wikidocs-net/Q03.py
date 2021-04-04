"""
    https://wikidocs.net/17114
    Q3 리스트의 더하기와 extend 함수
"""

a = [1, 2, 3]
print("a:", a)
print(id(a))
a = a + [4, 5]
print("a:", a)
print(id(a))
print("\n")

b = [1, 2, 3]
print("b:", b)
print(id(b))
b.extend([4, 5])
print("b:", b)
print(id(b))
