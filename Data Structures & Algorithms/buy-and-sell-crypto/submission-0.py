class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            curr_profit = prices[j] - prices[i]
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[j] < prices[i]:
                i = j
            j += 1
        return max_profit
            