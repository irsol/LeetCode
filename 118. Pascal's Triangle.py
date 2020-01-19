# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        output = []

        for r in range(numRows):
            row = [1] * (r + 1)
            for c in range(1, r):
                
                row[c] = output[r - 1][c -1] + output[r -1][c]
            output.append(row)
        return output 


      """
        output = []
        for row in range(numRows):
            output.append(1)

            for i in range(row - 1, 0, -1):
              output[i] += output[i - 1]
            print(*output)
      """