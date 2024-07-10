class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        curr = 0
        for n in nums:
            if n==1:
                curr+=1
            elif n==0:
                res = max(res,curr)
                curr = 0
        return max(res,curr)
        # return max([len(s) for s in (''.join([str(x) for x in nums])).split('0')])