class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        h = dict(sorted(h.items(), key=lambda x: x[1], reverse=True))
        res = []
        for item in h:
            if len(res) == k:
                return res
            res.append(item)
        return res
