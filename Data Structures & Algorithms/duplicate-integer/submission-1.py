class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setN = set()
        for num in nums: 
            if num in setN:
                return True
            setN.add(num)
        return False