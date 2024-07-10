class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = dict()

        for i in range(len(nums2) - 1, -1, -1):
            n = nums2[i]

            while len(stack) and stack[-1] <= n:
                stack.pop()
            
            ans[n] = stack[-1] if len(stack) else -1

            stack.append(n)

        return [ans[x] for x in nums1]