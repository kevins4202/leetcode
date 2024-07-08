class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = set(nums)
        return [x for x in range(1, n + 1) if x not in st]