class Solution:
    def rob(self, nums: List[int]) -> int:

        def _rob(i, memo):
            if i in memo:
                return memo[i]
            if len(nums) <= i:
                return 0
            memo[i] = max(nums[i] + _rob(i + 2, memo), _rob(i + 1, memo))
            return memo[i]

        return _rob(0, {})