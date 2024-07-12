class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        freqs = collections.Counter(nums)

        for n, f in freqs.items():
            if n + 1 in freqs:
                ans = max(ans, f + freqs[n+1])
        
        return ans