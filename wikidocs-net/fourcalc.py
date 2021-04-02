"""
    https://wikidocs.net/28
    Class, Input, String

    Day 2 (4/2)
"""

class FourCalc:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCalc(FourCalc):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCalc(MoreFourCalc):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second



#a = SafeFourCalc(4,0)

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
a = SafeFourCalc(first, second)
print("%d + %d = %d" % (first, second, a.add()))
print("%d - %d = %d" % (first, second, a.sub()))
print("%d * %d = %d" % (first, second, a.mul()))
print("%d / %d = %d" % (first, second, a.div()))
print("%d ** %d = %d" % (first, second, a.pow()))


