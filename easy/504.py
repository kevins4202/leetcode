class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        ans = "-" if num < 0 else ""

        n = abs(num)

        tmp = ""
        while n:
            tmp += str(n % 7)
            n //= 7
            # print(n)
        
        return ans + tmp[::-1]

