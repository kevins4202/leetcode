class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = -1
        for y, cnt in collections.Counter(nums).items():
            if cnt == 2:
                x = y
                break

        return [x , list(set(range(1, len(nums) + 1)) - set(nums))[0]]