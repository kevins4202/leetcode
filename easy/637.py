# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        cnt = 0
        total = 0
        ans = []

        currL = 0

        queue = [[root, 0]]

        while queue:
            curr = queue.pop(0)

            if curr[1] != currL:
                ans.append(total / cnt)
            
                total = 0
                cnt = 0
                currL = curr[1]
            
            total += curr[0].val
            cnt+=1

            if curr[0].left: queue.append([curr[0].left, curr[1]+1])
            if curr[0].right: queue.append([curr[0].right, curr[1]+1])
        ans.append(total / cnt)
        return ans