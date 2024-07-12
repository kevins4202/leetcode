class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def rec(n):
            if not n:
                return
            res.append(n.val)
            for c in n.children:
                rec(c)
        rec(root)
        return res