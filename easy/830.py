class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        lo = 0
        hi = 0

        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                if hi - lo + 1 >= 3:
                    ans.append([lo, hi])
                
                lo = i + 1
                hi = i + 1
            else:
                hi += 1
        
        if hi - lo + 1 >= 3:
            ans.append([lo, hi])

        return ans