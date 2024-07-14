# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        # self.ans = set()

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root: return -1

        return self.secondMin(root, root.val)

    def secondMin(self, root, mini):
        if not root: return -1

        if root.val > mini: return root.val

        leftMin = self.secondMin(root.left, mini)
        rightMin = self.secondMin(root.right, mini)

        if leftMin == -1 or rightMin == -1:
            return max(leftMin, rightMin)

        return min(leftMin, rightMin)