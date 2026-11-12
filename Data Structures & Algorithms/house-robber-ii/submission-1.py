class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge cases to consider
        # if we take the first house, we can't take the last house
        # if we skip the first house, we can take the last house

        def _rob(i, end, memo):
            if i in memo:
                return memo[i]
            if end <= i:
                return 0
            memo[i] = max(nums[i] + _rob(i + 2, end, memo), _rob(i + 1, end, memo))
            return memo[i]

        return max(nums[0] + _rob(2, len(nums) - 1, {}), _rob(1, len(nums), {}))
