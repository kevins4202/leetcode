class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        ans = 0

        if len(bed) == 0: return n == 0
        if len(bed) == 1: return 1-bed[0] >= n


        if bed[0] == 0 and bed[1] == 0:
            ans+=1
            bed[0] = 1

        
        for i in range(1, len(bed) - 1):
            if bed[i-1] == 0 and bed[i+1] == 0 and bed[i] == 0:
                ans+=1
                bed[i] = 1

        if bed[-1] == 0 and bed[-2] == 0:
            ans+= 1
            bed[-2] = 1

        return ans >= n