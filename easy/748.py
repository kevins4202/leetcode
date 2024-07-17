class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key = lambda w: len(w))

        s = ''.join([c.lower() for c in licensePlate if c.isalpha()])

        print(s)

        cnt = [0] * 26

        for c in s: 
            cnt[ord(c) - ord('a')]+=1

        for word in words:
            curr = [0] * 26
            for c in word:
                curr[ord(c) - ord('a')]+=1

            ok = True

            for c in s: 
                if cnt[ord(c) - ord('a')] > curr[ord(c) - ord('a')]:
                    ok = False
                    break
            
            if ok: return word
        return ""