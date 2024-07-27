class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0,1,1]

        if n < 3: return trib[n]

        for i in range(3, n):
            tmp = sum(trib)
            trib[0] = trib[1]
            trib[1] = trib[2]
            trib[2] = tmp

        return sum(trib)