class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) # array that stores product of all elements except nums[i]
        prev = 1
        for i in range(len(nums)):
            output[i] *= prev
            prev *= nums[i]
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= prev
            prev *= nums[i]
        return output
