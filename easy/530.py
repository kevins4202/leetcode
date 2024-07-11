# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 100000
        self.prev = -100000
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        
        self.ans = min(self.ans, abs(root.val - self.prev))
        self.prev = root.val

        self.inorder(root.right)


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)

        return self.ans