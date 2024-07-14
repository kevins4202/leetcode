class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = [0] * 128
        for c in moves:
            cnt[ord(c)]+=1
        
        return cnt[ord('U')] == cnt[ord('D')] and cnt[ord('L')] == cnt[ord('R')]