from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # this hash map will map Counter to the words
        for word in strs:
            tup = tuple(sorted(Counter(word).items()))
            if tup not in res:
                res[tup] = [word]
            else:
                res[tup].append(word)
        return [val for val in res.values()]