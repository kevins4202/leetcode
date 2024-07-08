class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        ans = 0

        chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

        for c in chars:
            print(c)
            cnt = s.count(c)

            odd = odd or bool(cnt & 1) 
            ans += (cnt - (cnt & 1))
        
        return ans + int(odd)
