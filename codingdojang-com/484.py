"""
    https://codingdojang.com/scode/484
    CamelCase를 Potheole_case로 바꾸기
"""

def ctop(l):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    r = ""
    for c in l:
        if c in a:
            r += "_" + c.lower()
        else:
            r += c
    return r


s = input("Enter CamelCase : ")
print(ctop(s))
