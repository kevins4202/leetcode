class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = set(candyType)

        return min(len(candies), len(candyType)//2)