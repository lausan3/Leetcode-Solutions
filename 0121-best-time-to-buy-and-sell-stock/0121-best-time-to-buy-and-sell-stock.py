class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window problem, we need two pointers both starting at the beginning
        l, r = 0, 1
        maxProfit = 0

        # then, we iterate through the array and adjust the pointers based on the value of what we're checking
        # until the right pointer has gone to the end
        while r < len(prices):
            profit = prices[r] - prices[l]

            # check profit
            ## if profit is negative, it means we have found a new low point for our stock so we adjust it to the right
            ## pointer
            if profit < 0:
                l = r
            # else, we have found a profitable day to buy and sell and we take the max of those two values
            else:
                maxProfit = max(maxProfit, profit)
            
            r += 1

        return maxProfit