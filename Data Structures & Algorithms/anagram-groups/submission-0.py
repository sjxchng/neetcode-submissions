class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {} # maps each count to a list
        for str in strs:
            count = [0] * 26 # list with 26 entries
            for s in str:
                asc = ord(s) - ord("a") # ascii value of current char
                count[asc] += 1
            key = tuple(count)
            if key not in h:
                h[key] = []
            h[key].append(str)
        return list(h.values())