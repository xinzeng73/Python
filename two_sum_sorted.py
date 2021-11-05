#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

numbers = [2,7,11,15]
target = 9

def twoSum(numbers, target):
    j=len(numbers)-1
    for i in range(j):
        tmp=target-numbers[i]
        l=i+1
        r=j
        while l <= r:
            m = l+(r-l)//2
            if numbers[m]==tmp:
                return i+1, m+1
            elif numbers[m] < tmp:
                l=m+1
            elif numbers[m] > tmp:
                r=m-1

print(twoSum(numbers, target))


