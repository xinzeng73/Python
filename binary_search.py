#https://leetcode.com/problems/binary-search/

nums = [-10,-9,-8,-7,-6,0,1,2,3,4,5,6,7,8,9,10]
target = 9


def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return None
x=search(nums, target)
if x != -1:
    print(f'Taget:{target} is at index{x}: {nums[x]}')

'''
The logic is that, 
key is the list is sorted, so we can find a number in the middle.
if number in the middle greater than target, we only search from middle +1 to last.
and  if number in the middle less than target, then only search from start 0(far left) to  middle-1.
Repeat this change to the left and right value which used in while logic until find the target.
'''
