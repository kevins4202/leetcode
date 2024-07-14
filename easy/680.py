class Solution:
    def isPal(self, s):
        return s == s[::-1]
    def validPalindrome(self, s: str) -> bool:
        flag = False
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                sub1 = s[i : j]
                sub2 = s[i+1: j + 1]

                return self.isPal(sub1) or self.isPal(sub2)
            i += 1
            j -= 1

        return True
