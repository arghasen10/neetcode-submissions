class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def dp(n):
            if n < 0:
                return 0
            if n <= 1:
                return 1
            if n in mem:
                return mem[n]
            mem[n] = dp(n-1) + dp(n-2)
            return mem[n]

        return dp(n)
