class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def rec(n):
            if not n:
                return
            
            for c in n.children:
                rec(c)
            res.append(n.val)
        rec(root)
        return res