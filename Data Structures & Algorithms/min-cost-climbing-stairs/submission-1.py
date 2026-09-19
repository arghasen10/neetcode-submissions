class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        n = len(cost)

        def dp(i):
            if i >= n:
                return 0
            if i in mem:
                return mem[i]
            mem[i] = cost[i] + min(dp(i+1), dp(i+2))
            return mem[i]
        return min(dp(0), dp(1))


