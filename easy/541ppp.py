class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), 2*k):
            s = s[0:i] + s[i:i+k][::-1] + s[i+k:len(s)]
        return s
            
        