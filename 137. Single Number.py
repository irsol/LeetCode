# Given a non-empty array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
#
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,3,2]
# Output: 3


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        newlst = list(set(nums))
        for num in newlst:
            if nums.count(num) == 1:
                return num
            continue
        return None

     