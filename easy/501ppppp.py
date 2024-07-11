class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: [TreeNode]) -> List[int]:
        curr = root
        result = []
        curr_streak = 0
        max_streak = 0
        curr_num = float("inf")

        while curr:
            if curr.left:
                neighbor = curr.left
                while neighbor.right:
                    neighbor = neighbor.right
                
                neighbor.right = curr
            
                tmp = curr.left
                curr.left = None
                curr = tmp
            else:
                if curr.val == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 0
                    curr_num = curr.val
                
                if curr_streak == max_streak:
                    result.append(curr_num)
                elif curr_streak > max_streak:
                    max_streak = curr_streak
                    result = [curr_num]
                
                curr = curr.right
        return result