class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        curr = 1
        prev = 0

        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                print(f'{curr} {prev}')
                ans += min(curr, prev)
                prev = curr
                curr = 1
            else: curr += 1
        
        return ans + min(curr, prev)