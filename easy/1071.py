class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""

        a, b = len(str1), len(str2)
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                tmp1 = str1[:i]
                tmp2 = str2[:i]

                if tmp1 == tmp2 and tmp1 * (a // i) == str1 and tmp2 * (b // i) == str2: ans = tmp1

        return ans