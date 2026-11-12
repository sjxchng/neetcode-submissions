class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge cases to consider
        # if we take the first house, we can't take the last house
        # if we skip the first house, we can take the last house

        def _rob(i, rob_first, memo):
            if i in memo:
                return memo[i]
            if rob_first:
                if len(nums) - 1 <= i:
                    return 0
                memo[i] = max(nums[i] + _rob(i + 2, True, memo), _rob(i + 1, True, memo))
                return memo[i]
            else:
                if len(nums) <= i:
                    return 0
                memo[i] = max(nums[i] + _rob(i + 2, False, memo), _rob(i + 1, False, memo))
                return memo[i]

        return max(nums[0] + _rob(2, True, {}), _rob(1, False, {}))
