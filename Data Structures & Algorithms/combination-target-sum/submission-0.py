class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, tmp = [], []
        nums.sort()
        def dfs(i):
            # fix 1: base case can come after the check
            # check if found valid target
            if sum(tmp) == target:
                res.append(tmp[:]) # fix 2: pass in a copy
                return
            # base case
            if i == len(nums) or sum(tmp) > target:
                return
            
            # fix 3: you only need 2 branches, not 3
            
            # skip this number, go next
            dfs(i + 1)
            # add this number, stay here
            tmp.append(nums[i])
            dfs(i)
            tmp.pop()

        dfs(0)
        return res