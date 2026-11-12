class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1, h2 = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            h1[c1] = h1.get(c1, 0) + 1
            h2[c2] = h2.get(c2, 0) + 1
        return h1 == h2