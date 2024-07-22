class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0

        for j in range(len(strs[0])):
            curr = [strs[i][j] for i in range(len(strs))]

            if curr != sorted(curr): cnt += 1
        
        return cnt