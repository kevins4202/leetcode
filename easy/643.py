class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        tmp = ans

        for i in range(k, len(nums)):
            tmp = tmp - nums[i-k] + nums[i]

            ans = max(ans, tmp)

        return ans / k