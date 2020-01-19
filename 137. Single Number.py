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
        
      # Runtime: 1348 ms, faster than 5.06% of Python online submissions for Single Number II.
      # Memory Usage: 13.8 MB, less than 45.45% of Python online submissions for Single Number II.

        # convert to a set then back to a list
        new_lst = list(set(nums)) 
        
        for num in new_lst:
          # check if exists in new_lst or not
            if nums.count(num) == 1:
                return num
        return None

     