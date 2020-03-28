# 217. Contains Duplicate 
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in
# the array, and it should return false if every element is distinct.

# Runtime: 100 ms, faster than 91.41% of Python online submissions for Contains Duplicate.
# Memory Usage: 18 MB, less than 5.55% of Python online submissions for Contains Duplicate.

class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set()

        for x in nums:
            if x in nums_set:
                return True
            nums_set.add(x)            
        return False
