# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def calculateDiameter(self, root, d):
        if not root: return 0

        leftHeight = self.calculateDiameter(root.left, d)
        rightHeight = self.calculateDiameter(root.right, d)

        self.diameter = max(self.diameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateDiameter(root, self.diameter)

        return self.diameter