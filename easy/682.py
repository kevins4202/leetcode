class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for x in ops:
            if x == "+":
                ans.append(ans[-1] + ans[-2])
            elif x == "C":
                ans.pop()
            elif x == "D":
                ans.append(2 * ans[-1])
            else:
                ans.append(int(x))
                

        return sum(ans) 