"""
    https://codingdojang.com/scode/408
    1차원의 점들이 주어졌을때, 그중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오
    S={1,3,4,5,13,17,20}
    (3,4))
"""


def findShort(arr):
    r = 9999
    r_arr = []
    for i in range(0,len(arr)-1):
        m = arr[i+1]-arr[i]
        if m<=r :
            r=m
            s_arr = [arr[i], arr[i+1]]
            r_arr.append(s_arr)
    return(r_arr)

#S = [1,3,4,5,13,17,20]
S = [1,3,7,13,17,20,22,24]
print(findShort(S))
