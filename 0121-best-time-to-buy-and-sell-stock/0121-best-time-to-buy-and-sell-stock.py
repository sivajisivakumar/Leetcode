class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        j=0
        profit=0
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
            else:
                profit=max(profit,prices[j]-prices[i])
            j+=1
        return profit
        