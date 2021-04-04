"""
    https://wikidocs.net/17114
    Q1 문자열 바꾸기

"""

s = "a:b:c:d"
sps = s.split(":")
new_s = "#".join(sps)

"""
new_s = ""
for sp in sps:
    new_s = new_s + "#" + sp
"""

print (new_s)
