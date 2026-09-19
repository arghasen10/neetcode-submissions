class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [3,2,6,5,0,3]
        left_profit = [prices[0]]*(len(prices)+1)      #[3,2,6,5,0,3]
        right_profit = [prices[-1]]*(len(prices)+1)    #[4,4,4,4,4,4]
        for i in range(1,len(prices)):
            left_profit[i] = min(left_profit[i-1], prices[i-1])  #[3,3,2,2,2,0,0]
        left_profit[len(prices)] = left_profit[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            right_profit[i+1] = max(right_profit[i+2], prices[i+1]) #[6,6,6,5,3,3,3]
        right_profit[0] = right_profit[1]
        profit = 0
        for i in range(len(prices)):
            new_profit = right_profit[i]-left_profit[i]
            if new_profit < profit:
                continue
            profit = new_profit
        return profit
        1,0
        [1,4,2]
        [1,1,1,1]
        [4,4,2,2]
        