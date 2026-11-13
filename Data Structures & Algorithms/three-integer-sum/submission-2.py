class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # first value
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # second and third values
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[l] + nums[r] + nums[i]
                if summ == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                elif summ < 0:
                    l += 1
                elif 0 < summ:
                    r -= 1

        return res
