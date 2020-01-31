# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.

# Examples:
"""
s = "leetcode"
return 0.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Second Solution
        count = {}
        for char in s:
          if char not in count:
            count[char] = 0
          count[char] += 1
        for char in s:
          if count[char] == 1:
            return s[:-1]

        # First Solution
        # Runtime: 5292 ms, faster than 5.07% of Python online submissions for First Unique Character in a String.
        # Memory Usage: 13 MB, less than 23.91% of Python online submissions for First Unique Character in a String.
        for i in range(len(s)):
          ch = s[i]
          if s.count(ch) == 1:
            return(i)
        return(-1)
