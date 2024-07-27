class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        i = 0

        while i < len(nums) and k > 0:
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
                i += 1
            else:
                break

        nums = sorted(nums)
        
        if k % 2 == 1:
            nums[0] *= -1
        
        return sum(nums)