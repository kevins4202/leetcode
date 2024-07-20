class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left = [0] * len(s)
        right = [0] * len(s)

        curr = -100000

        for i in range(len(s)):
            if s[i] == c:
                curr = i
            
            left[i] = curr
        
        curr = -100000
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                curr = i
            
            right[i] = curr

        ans = [0] * len(s)

        for i in range(len(s)):
            ans[i] = min(abs(left[i] - i), abs(right[i] - i))
        
        return ans