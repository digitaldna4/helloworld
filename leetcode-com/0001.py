"""
    https://leetcode.com/problems/two-sum/
    1. Two Sum
    Easy
"""


def twosum(nums, target):
    for i in range(0, len(nums)):
        num = nums[i]
        for j in range (i+1, len(nums)):
            if(nums[j] + num == target):
                return [i, j]
        i += 1

#Test
nums = [2,7,11,15]
target = 26
print("nums",nums)
print("target",target)
print(twosum(nums,target))


