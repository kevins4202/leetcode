class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""

        if num < 0:
            num += pow(2,32)
        
        while num:
            curr = num % 16

            if curr > 9:
                ans += chr(ord('a') + curr - 10)
            else:
                ans += str(curr)

            num //= 16
        
        return ans[::-1]