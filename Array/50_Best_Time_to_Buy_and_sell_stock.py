


# ============================================================================
# Name        : 50_Best_Time_to_Buy_and_sell_stock.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        min_Value = 1000000
        index  = 0
        for i in range(0,len(prices)):
            if prices[i] < min_Value:
                min_Value,index = prices[i],i
        print(min_Value,index)
        max_val = 0
        for j in range(index,len(prices)):
            if prices[j] > max_val:
                max_val = prices[j]
        print(min_Value,index,max_val)
        return max_val - min_Value
        # solution accepted but one case failed
        if len(prices) == 0 or len(prices) == 1:
            return 0
        else:
            profit = 0
            for i in range(len(prices) - 1):
                for j in range(i + 1, len(prices)):
                    if (prices[j] - prices[i]) > profit:
                        profit = (prices[j] - prices[i])
            return profit
            """
        # accepted solution
        # find the length of array if its less than 1 return 0
        if len(prices) == 0 or len(prices) == 1: return 0

        max_profit = 0
        min_price = prices[0]
        # for each value in prices find minimum,difference and max value
        for price in prices:
            min_price = min(min_price,price)
            comp_profit = price - min_price
            max_profit = max(max_profit,comp_profit)
        return max_profit


if __name__ == '__main__':
    n = [7,1,5,3,6,4]
    test = Solution()
    out = test.maxProfit(n)
    print(out)
