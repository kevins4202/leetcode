# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.leaf1 = []
        self.leaf2 = []
    def leaves(self, root, first):
        if not root: return

        self.leaves(root.left, first)
        if not root.left and not root.right:
            if first: self.leaf1.append(root.val)
            else: self.leaf2.append(root.val)
        self.leaves(root.right, first)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaves(root1, 1)
        self.leaves(root2, 0)

        return len(self.leaf1) == len(self.leaf2) and all(self.leaf1[i] == self.leaf2[i] for i in range(len(self.leaf1)))