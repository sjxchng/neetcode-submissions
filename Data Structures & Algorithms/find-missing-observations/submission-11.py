class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mis_tot = mean * (n + len(rolls)) - sum(rolls)

        # check if a valid combination is available
        if mis_tot < n or 6*n < mis_tot:
            return []

        res = [mis_tot // n] * n # initial res array with missing total evenly divided
        for i in range(mis_tot % n): # add the leftovers
            res[i] += 1
        return res

        