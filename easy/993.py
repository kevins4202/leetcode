# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthOf(self, root, tar):
        queue = [[root, 0]]

        while queue:
            curr = queue.pop()

            node = curr[0]
            depth = curr[1]

            if node.left:
                if node.left.val == tar:
                    return curr

                queue.append([node.left, depth + 1])

            if node.right:
                if node.right.val == tar:
                    return curr
                
                queue.append([node.right, depth + 1])
        
        return None
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        one = self.depthOf(root, x)
        two = self.depthOf(root, y)

        if not one or not two: return False

        print(f'{one[0].val} {two[0].val}')

        return one[0] != two[0] and one[1] == two[1]