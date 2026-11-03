class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            count = tuple(count)
            if count not in h:
                h[count] = [s]
            else:
                h[count].append(s)
        return [value for value in h.values()]

