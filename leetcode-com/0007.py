"""
    https://leetcode.com/problems/reverse-integer/
    7. Reverse Integer
    Easy
"""

def reverseInt(i):
    i = int(i)
    s = str(abs(i))
    s_n = ""
    for j in range(len(s)-1,-1,-1):
        #s_n.extend(s[j])
        s_n += s[j]
        #print("s_n", s_n)
    
    if i<0:
        return int(s_n) * -1
    else:
        return s_n

#input = -987
in_key = input("Enter number: ")
print("Input :", in_key)
#print(input)
print("Output :", reverseInt(in_key))


"""
def reverse(self, x: int) -> int:
    if x>0: #Positive
        value=int(str(x)[::-1]) #reversed
    else: #Negative and zero
        value=-1*int(str(x*-1)[::-1])  #reversed
    
    if value not in range(-2**31,2**31): #Overflow 
        value=0
    
    return value
"""