"""
    https://leetcode.com/problems/palindrome-number/
    9. Palindrome Number
    Easy
"""


def palindNum(num_in:int):
    num_in = int(num_in)
    """
    s = str(num_in)
    s_new = ""
    for i in range(len(s)-1, -1, -1):
        s_new += s[i]
    print("s_new", s_new)
    if s == s_new:
        return True
    else:
        return False


    """
    # without string conversion
    if num_in == 0:
        return True
    if num_in < 0 or num_in % 10 == 0:
        return False
    rev = 0
    temp = num_in
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
    return rev == num_in


key_in = input("Enter Number: ")
print("Key_in", key_in)
print(palindNum(key_in))




