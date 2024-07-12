class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # print(root.children)
        if not root: return 0

        def dfs(node, depth):
            if not node.children: return depth
            return max(dfs(child, depth + 1) for child in node.children)
        
        return dfs(root, 1)
