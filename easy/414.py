class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        first = second = third = -pow(2,32)

        for x in nums:
            if x > first:
                third = second
                second = first
                first = x
            elif x > second and x < first:
                third = second
                second = x
            elif x > third and x < second:
                third = x
        
        if len(nums) < 3 or first == second or second == third or first == -pow(2,32) or second == -pow(2,32) or third == -pow(2,32):
            return first
        else:
            return third