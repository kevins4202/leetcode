class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        
        curr = ""
        while n:
            curr += str(n % 2)
            n //= 2

        curr = ''.join(str(1 - int(c)) for c in curr)

        p = 1

        ans = 0
        for c in curr:
            ans += p * int(c)

            p *= 2
        
        return ans