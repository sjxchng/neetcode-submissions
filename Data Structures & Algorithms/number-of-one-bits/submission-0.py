class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1:
                res += 1
            n = n >> 1
        return res
    
    # more optimal trick, but not absolutely necessary
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & n - 1
            res += 1
        return res