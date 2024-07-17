class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ns = list(enumerate(nums))
        ns = sorted(ns, key = lambda x: x[1])

        return ns[-1][0] if ns[-2][1] * 2 <= ns[-1][1] else -1