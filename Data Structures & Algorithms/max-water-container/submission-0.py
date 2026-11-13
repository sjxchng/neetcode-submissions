class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
    
    def maxArea(self, heights: List[int]) -> int:
        # optimized
        # key thing I had to sit with:
        # remove the taller wall -> we're guaranteed to have smaller area
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res