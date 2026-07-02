class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            # 5/Hello5/World
            res += str(len(string)) + "/" + string
        return res
            
    def decode(self, s: str) -> List[str]:
        res = []
        numCount = 0
        num = 0
        i = 0
        # i < 14
        while i < len(s):
            if s[i] == "/":
                num = int(s[i - numCount : i])
                i += 1
                res.append(s[i : i + num])
                i += num
                numCount = 0
            else:
                numCount += 1
                i += 1
        return res
            
