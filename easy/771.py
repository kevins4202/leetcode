class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jews = set(jewels)

        ans = 0

        for x in stones:
            if x in jews:
                ans+=1
        return ans