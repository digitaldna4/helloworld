"""
    https://wikidocs.net/17114
    Q08 역순 저장
"""

f = open("Q08.txt", 'r')
lines = f.readlines()
f.close()
#print("lines", lines)
#lines_new = lines.reverse()
#print("lines 2nd", lines)
lines.reverse()

f = open("Q08_new.txt", 'w')
print("lines_new", lines)
for line in lines:
    line = line.strip()
    f.write(line)
    f.write("\n")
f.close()
