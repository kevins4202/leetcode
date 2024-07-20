class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        curr = 0

        ans = 0

        while n:
            if n % 2 == 1:
                if prev != -1:
                    ans = max(ans, curr - prev)
                
                prev = curr
            
            curr+=1
            n//=2
        return ans