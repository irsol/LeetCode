# Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1


class Solution(object):
    def singleNumber(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      s = set()
      for num in nums:
          if num in s:
              s.remove(num)
          else:
              s.add(num)
      return s.pop()