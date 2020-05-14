'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def TwoSum(nums,target):
    h = {}
    for i,n in enumerate(nums):
        temp = target - n
        if temp not in h:
            h[n] = i
        else:
            return[h[temp],i]

if __name__ == "__main__":
    print(TwoSum([3,2,4],6))