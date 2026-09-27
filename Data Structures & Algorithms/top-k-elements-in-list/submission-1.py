class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {} # maps number to its occurences
        for num in nums:
            h[num] = h.get(num, 0) + 1
        # [0, 1, 2,..., len(nums)]
        l = [[] for _ in range(len(nums) + 1)]
        for key in h:
            l[h[key]].append(key)
        
        res = []
        for i in range(len(l) - 1, -1, -1):
            for n in l[i]:
                if len(res) == k:
                    return res
                res.append(n)
        return res