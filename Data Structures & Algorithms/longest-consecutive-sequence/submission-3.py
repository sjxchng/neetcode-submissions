class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            count = 1
            i = 1
            # VERY IMPORTANT: only count down when it's the end of a sequence
            if num + 1 not in s:
                while num - i in s:
                    count += 1
                    i += 1
            res = max(res, count)
        return res


