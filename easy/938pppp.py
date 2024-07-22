# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        if not root: return 0

        if root.val < lo: return self.rangeSumBST(root.right, lo, hi)
        elif root.val > hi: return self.rangeSumBST(root.left, lo, hi)
        else: return root.val + self.rangeSumBST(root.right, lo, hi) + self.rangeSumBST(root.left, lo, hi)
