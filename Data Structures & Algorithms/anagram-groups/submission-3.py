# added
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            c = tuple(sorted(Counter(word).items()))
            if c not in h:
                h[c] = []
            h[c].append(word)
            
        return [value for value in h.values()]