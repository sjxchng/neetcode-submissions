class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, tmp = [], []
        def dfs(i):
            if i == len(nums):
                res.append(tmp.copy())
                return

            # branch to subset w/out nums[i]
            dfs(i + 1)

            # branch to subset with nums[i]
            tmp.append(nums[i])
            dfs(i + 1)
            tmp.pop()

        dfs(0)
        return res