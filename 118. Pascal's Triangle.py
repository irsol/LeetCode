# 118. Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
      # Runtime: 20 ms, faster than 43.27% of Python online submissions for Pascal's Triangle.
      # Memory Usage: 11.8 MB, less than 30.00% of Python online submissions for Pascal's Triangle.

        output = []

        for r in range(numRows):
            row = [1] * (r + 1)
            for c in range(1, r):                
                row[c] = output[r - 1][c - 1] + output[r - 1][c]
            output.append(row)
        return output
