# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, node: TreeNode) -> TreeNode:
        dummy = tail = TreeNode()

        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                predecessor.right = node
                left, node.left = node.left, None

                node = left

            else:
                tail.right = tail = node
                node = node.right
        return dummy.right