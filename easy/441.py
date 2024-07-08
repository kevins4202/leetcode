class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        lo = 1
        hi = n

        while lo < hi:
            mid = lo + (hi - lo)//2

            curr = mid * (mid + 1) //2

            if curr == n:
                return mid
            elif curr < n:
                lo = mid + 1
            else:
                hi = mid

        return lo - 1
            