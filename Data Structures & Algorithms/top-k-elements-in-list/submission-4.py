class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in h.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for item in bucket[i]:
                res.append(item)
                if len(res) == k:
                    return res
