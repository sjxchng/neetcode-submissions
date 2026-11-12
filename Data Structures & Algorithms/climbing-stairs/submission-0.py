class Solution:
    def climbStairs(self, n: int) -> int:

        def ways(n, memo):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1
            memo[n] = ways(n - 1, memo) + ways(n - 2, memo)
            return memo[n]
    
        return ways(n, {})