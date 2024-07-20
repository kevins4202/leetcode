class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []


        for c in s:
            print(c)
            if c == '#':
                if len(s1) > 0:
                    s1.pop()
            else:
                s1.append(c)

        for c in t:
            if c == '#':
                if len(s2) > 0:
                    s2.pop()
            else:
                s2.append(c)

        # print(s1)
        # print(s2)
        
        return ''.join(s1) == ''.join(s2)