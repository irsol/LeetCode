# 242. Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Runtime: 40 ms, faster than 71.25% of Python online submissions for Valid Anagram.
# Memory Usage: 13.3 MB, less than 15.79% of Python online submissions for Valid Anagram.

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)