class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if p<prices[j]-prices[i]:
                    p=prices[j]-prices[i]
        return p