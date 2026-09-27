class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        # input: 5#Hello5#World
        while i < len(s):
            length_idx = i
            while s[length_idx] != "#":
                length_idx += 1
            value = int(s[i : length_idx])
            res.append(str(s[length_idx + 1 : length_idx + 1 + value]))
            i = length_idx + 1 + value
        return res