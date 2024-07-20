class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        
        s1 = set(aliceSizes)

        delta = (sum2 - sum1) //2

        for x in bobSizes:
            y = x - delta

            if y in s1:
                return [y, x]

        return []