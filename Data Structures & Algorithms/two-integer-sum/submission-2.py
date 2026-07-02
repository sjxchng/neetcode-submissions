class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            want = target - n
            if want in hash:
                return [hash[want], i]
            hash[n] = i