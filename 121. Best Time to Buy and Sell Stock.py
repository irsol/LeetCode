import unittest
# 121. Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell
# one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
            # Not 7-1 = 6, as selling price needs to be larger than buying price.


class unitest(unittest.TestCase):
    def testEmptyList(self):
        input = []
        output = 0
        self.assertEqual(Solution().maxProfit(input), output)
    def test_a(self):
        input = [7,1,5,3,6,4]
        output = 5
        self.assertEqual(Solution().maxProfit(input), output)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0 
        
        min_price = prices[0]
        max_profit = 0
        
        for n in prices:
            if n < min_price:
                min_price = n
            elif max_profit < n - min_price:
                max_profit = n - min_price
        return max_profit

if __name__ == '__main__':
    unittest.main()