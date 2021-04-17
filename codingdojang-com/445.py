"""
    https://codingdojang.com/scode/445
    비슷한 단어 찾기
    Lv. 2
    
    OneEditApart("cat", "dog") = false
    OneEditApart("cat", "cats") = true

    202010414
    (완성 못함)
"""

def OneEditApart(s1, s2):
    if len(s1) == len(s2):
        #
        for i in range(len(s1)):
            chk = 0
            if s1[i] != s2[i]:
                chk += 1
            if chk <= 1:
                return True
            else:
                return False
    elif abs(len(s1)-len(s2)) == 1:
        #
        for i in range(len(s1)):
            #
    else:
        return false


    

