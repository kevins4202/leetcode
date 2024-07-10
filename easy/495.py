class Solution:
    def findPoisonedDuration(self, t: List[int], dur: int) -> int:
        ans = 0
        for i in range(0, len(t) - 1):
            start = t[i]
            nex = start + dur - 1

            if t[i+1] <= nex:
                ans += (t[i+1] - t[i])
            else:
                ans += dur

        return ans + dur