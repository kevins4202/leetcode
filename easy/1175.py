class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        notPrime = [0] * 101

        notPrime[1] = 1
        for i in range(2, 101):
            if notPrime[i]: continue
            curr = 2*i
            while curr <= 100:
                notPrime[curr] = 1
                curr += i

        # for i in range(2, 101): 
        #     if notPrime[i]: 
        #         print(i)
        
        primes = sum(notPrime[:n+1])
        nons = n - primes

        print(f'{primes} {nons}')

        ans = 1
        while primes:
            ans = (ans * primes) % (1000000007)
            primes -= 1
        while nons:
            ans = (ans * nons) % (1000000007)
            nons -= 1

        return ans