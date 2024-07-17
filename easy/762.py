class Solution:
    def bits(self, num):
        cnt = 0
        while(num > 0):
            cnt += (num % 2)
            num //=2

        return cnt


    def countPrimeSetBits(self, left: int, right: int) -> int:
        num = 665772
        ans = 0

        for x in range(left, right + 1):
            if 1 << x.bit_count() & num:
                ans += 1
        return ans