# 231. Power of Two
# Given an integer, write a function to determine if it is a power of two.

# Example:
# Input: 16
# Output: true
# Explanation: 24 = 16

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