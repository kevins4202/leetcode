class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, x in enumerate(nums):
            if x in C: C[x].append(i)
            else: C[x] = [i]
        
        M = max([len(i) for i in C.values()])

        return min([i[-1] - i[0] for i in C.values() if len(i) == M]) + 1