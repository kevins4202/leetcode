class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        run = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                run += 1
                ans = max(run, ans)
            else:
                run = 1
        
        return max(ans, run)

