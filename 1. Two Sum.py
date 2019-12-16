# 1. Two Sum

# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.

# Runtime: 36 ms, faster than 76.63% of Python online submissions for Two Sum.
# Memory Usage: 13.1 MB, less than 46.92% of Python online submissions for Two Sum.

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_tb = {}
    for i, num in enumerate(nums):
        if target - num in hash_tb:
            return [hash_tb[target - num], i]
            
        hash_tb[num] = i
