class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums) # array with all left elements multiplied
        r = [1] * len(nums) # array with all right elements multiplied

        prev = 1
        for i in range(len(nums)):
            l[i] = prev
            prev *= nums[i]
        
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            r[i] = prev
            prev *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(l[i] * r[i])
        
        return res