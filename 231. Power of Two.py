# 231. Power of Two
# Given an integer, write a function to determine if it is a power of two.

# Example:
# Input: 16
# Output: true
# Explanation: 24 = 16

# Runtime: 16 ms, faster than 84.51% of Python online submissions for Power of Two.
# Memory Usage: 12.9 MB, less than 11.76% of Python online submissions for Power of Two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False
        while n%2 == 0:
            n = n/2
        return n == 1