class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')

        ans = s[:len(s) % k]

        for i in range(len(s) % k, len(s),k):
            if i != 0:
                ans += '-'
            for j in range(i, i + k):
                ans += s[j]
        return ans
        
