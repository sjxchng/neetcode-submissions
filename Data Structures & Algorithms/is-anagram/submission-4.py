class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        for a in s:
            hashS[a] = hashS.get(a, 0) + 1
        for b in t:
            hashT[b] = hashT.get(b, 0) + 1
        for c in hashS:
            if hashS[c] != hashT.get(c):
                return False
        return True