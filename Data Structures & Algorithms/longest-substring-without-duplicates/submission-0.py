class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window (l, r)
        # approach 1: keep a hash map with all counts
        # increase the window (r) if all counts are 1 or less
        # if not, then decrease the widnow until all counts are 1 or less (l)

        # example
        # z x y z z z
        #   l
        #       r

        # i'm currently thiking
        # instead of using a hashmap we can also use a set
        # when we move the left pointer, we can just pop the ones alr in set and
        # specifically for the element at the right pointer, we'll keep en eye out for that and
        # once left pointer is at that, we will increase one more time and then keep the element in the set 
        # since right pointer is there currently

        # i would add the element to the set whenever we see it, and remove it whenever we are moving the left pointer

        # if character already in the set

        # length of window would be r - l + 1

        # yes! I can implement that

        l, r = 0, 0
        h = set()
        res = 0
        while r < len(s):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
        

