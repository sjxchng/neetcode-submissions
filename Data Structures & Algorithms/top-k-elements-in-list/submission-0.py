class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {} # maps number to its occurences
        for num in nums:
            h[num] = h.get(num, 0) + 1
        
        # h = list of tuples (value, occurences)
        h = sorted(h.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(h[i][0])
        return res