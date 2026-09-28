class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            tmp_res = 1
            # only start counting down if it's the end of a sequence
            if num + 1 not in s:
                while num - 1 in s:
                    tmp_res += 1
                    num -= 1
            res = max(res, tmp_res)
        return res
