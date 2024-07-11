class Solution:
    def fib(self, n: int) -> int:
        ans = [0, 1, 1]

        if n < 3: return ans[n]

        for i in range(2, n):
            tmp = ans[1] + ans[2]
            ans[0] = ans[1]
            ans[1] = ans[2]
            ans[2] = tmp
            # print(f'{a} {b} {c}')

        return ans[2]