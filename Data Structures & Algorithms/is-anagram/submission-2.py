class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for a in s:
            if a in dict:
                dict[a] += 1
            else: 
                dict[a] = 1
        for b in t:
            if b in dict:
                dict[b] -= 1  
            else: 
                dict[b] = -1
        for value in dict.values():
            if value != 0:
                return False
        return True
        