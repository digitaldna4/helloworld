"""
    https://codingdojang.com/scode/465
    문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기
    aaabbcccccca
    a3b2c6a1
"""


s_in = str(input("Enter strings.. \n"))
result = ""
cnt = 1
for i in range(0, len(s_in)-1):
    if s_in[i] == s_in[i+1]:
        cnt += 1
    else:
        result = result + s_in[i] + str(cnt)
        cnt = 1

result = result + s_in[i+1] + str(cnt)

print(result)
