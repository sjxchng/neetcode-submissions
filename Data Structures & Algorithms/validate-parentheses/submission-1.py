class Solution:
    def isValid(self, s: str) -> bool:
        # ( -> )
        # { -> }
        # [ -> ]
        stack = []
        hashmap = {")":"(", "}":"{", "]":"["}
        for par in s:
            if par == "(" or par == "{" or par == "[":
                stack.append(par)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if not popped == hashmap[par]:
                    return False
        return True if not stack else False