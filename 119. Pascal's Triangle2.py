# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

# Example:

# Input: 3
# Output: [1,3,3,1]

# Runtime: 28 ms, faster than 11.28% of Python online submissions for Pascal's Triangle II.
# Memory Usage: 11.8 MB, less than 26.92% of Python online submissions for Pascal's Triangle II.

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        for x in range(1, rowIndex + 1):
          for y in range(x - 1, 0, -1):
            row[y] += row[y - 1]
        return row  