#https://leetcode.com/problems/two-sum/

numbers = [2,7,11,15]
target = 9

def twoSum(nums, target):
    dic={}
    for i,j in enumerate(nums):
        if target - j in dic:
            return dic[target-j], i
        else:
            dic[j]=i

print(twoSum(numbers, target))

