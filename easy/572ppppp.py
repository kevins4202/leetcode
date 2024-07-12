# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sameTree(self, root, sub):
        if (not root) and (not sub): return True
        if (not root) or (not sub):
            return False
        
        x = root.val
        y = sub.val

        return (x == y) and self.sameTree(root.left, sub.left) and self.sameTree(root.right, sub.right)
    def isSubtree(self, root, sub):
        if (not root):
            return False
        return self.sameTree(root, sub) or self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)
        