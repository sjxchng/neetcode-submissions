class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            count = int(count)
            i += 1 # skip the "#"
            strs.append(s[i : i + count])
            i += count
        return strs
