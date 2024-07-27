class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = [0] * 26

        for c in text:
            letters[ord(c) - ord('a')] += 1

        ans = 0

        ok = True

        while ok:
            for c in 'balloon':
                i = ord(c) - ord('a')
                if letters[i] == 0:
                    ok = False
                    break
                else:
                    letters[i] -= 1
            
            if ok: ans += 1
        
        return ans