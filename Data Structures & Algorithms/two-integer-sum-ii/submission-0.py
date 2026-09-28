class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ < target:
                l += 1
            elif target < summ:
                r -= 1
            else:
                # 1-indexed
                return [l + 1, r + 1]