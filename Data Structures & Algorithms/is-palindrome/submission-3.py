class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ""
        for c in s:
            if c.isalnum():
                alnum += c.lower()
        s = alnum

        # edge case
        if len(s) <= 1:
            return True

        mid = len(s) // 2
        # odd len
        l, r = mid, mid
        while 0 <= l and r <= len(s) - 1 and s[l] == s[r]:
            if l == 0 and r == len(s) - 1:
                return True
            l -= 1
            r += 1
        # even len
        l, r = mid - 1, mid
        while 0 <= l and r <= len(s) - 1 and s[l] == s[r]:
            if l == 0 and r == len(s) - 1:
                return True
            l -= 1
            r += 1
        
        return False

