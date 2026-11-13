class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window example w/ k = 2 replacements
        # Z Z Y X Y Y Y 
        #   l 
        #         r
        # h = {Z:1, Y:2, X:1}
        # res = r - l + 1

        # increase pointer r when 
        # other values (Z, X = 2) <= k (k = 2)

        # to compute this "other values", 
        # we can do r - l + 1 - maxFreq (Y = 2)
        
        # use a while loop
        # increase pointer l when 
        # other vlaues > k

        h = {}
        res = 0
        l, r = 0, 0
        maxFreq = 0
        while r < len(s):
            h[s[r]] = h.get(s[r], 0) + 1
            maxFreq = max(maxFreq, h[s[r]])
            while r - l + 1 - maxFreq > k:
                h[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

        