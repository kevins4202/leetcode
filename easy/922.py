class Solution:
    def sortArrayByParityII(self, s: list) -> list:
        i, j = 0, 1

        while i < len(s):
            while i < len(s) and s[i] % 2 == 0: i += 2
            while j < len(s) and s[j] % 2 == 1: j += 2

            if i < len(s): s[i], s[j] = s[j], s[i]

            i += 2
            j += 2

        return s