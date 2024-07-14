class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n % 2

        n //= 2

        while n:
            if n % 2 == prev: return False

            n //= 2
            prev = 1-prev

        return True