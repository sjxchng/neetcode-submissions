class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for a in s:
            if a in dictS:
                dictS[a] += 1  
            else: 
                dictS[a] = 1
        for b in t:
            if b in dictT:
                dictT[b] += 1  
            else: 
                dictT[b] = 1
        return dictS == dictT
        