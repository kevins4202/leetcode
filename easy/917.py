class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1

        s = list(s)

        while i < j:
            while i < len(s) and not s[i].isalpha(): i+=1

            while j >= 0 and not s[j].isalpha(): j -= 1

            if i >= j: break

            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1

        return ''.join(s)