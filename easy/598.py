class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x = m
        y = n

        for p in ops:
            x = min(x, p[0])
            y = min(y, p[1])

        return x * y