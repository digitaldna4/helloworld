"""
    https://wikidocs.net/17114
    Q2 딕셔너리 값 추출하기
"""

a = {"A":90, "B":80, "C":70}
print(a["C"])
print("---")

b = {"A":90, "B":80}
print(b.get("B",70))
print(b.get("C",70))


