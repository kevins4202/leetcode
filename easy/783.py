# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = 100000
        prev = -100000

        def rec(node):
            if not node: return
            
            nonlocal prev
            nonlocal ans

            rec(node.left)
            ans = min(ans, node.val - prev)
            prev = node.val
            rec(node.right)

        rec(root)

        return ans