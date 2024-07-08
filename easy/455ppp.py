class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        ans = 0

        for c in s:
            if c >= g[ans]:
                ans +=1
                if ans == len(g):
                    return ans 
        
        return ans