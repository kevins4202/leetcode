class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n+1)
        trustedBy = [0] * (n+1)

        for x in trust:
            a = x[0]
            b = x[1]

            trusts[a] += 1
            trustedBy[b] += 1
        
        for i in range(1, n+1):
            if trusts[i] == 0 and trustedBy[i] == n-1: return i
        
        return -1