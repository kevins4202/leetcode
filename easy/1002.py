class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = [0] * 26

        for c in words[0]:
            ans[ord(c) - ord('a')] += 1

        for word in words[1:]:
            tmp = [0] * 26
            for c in word:
                tmp[ord(c) - ord('a')] += 1

            for i in range(26):
                ans[i] = min(ans[i], tmp[i])
        
        ret = []

        for i in range(26):
            for c in range(ans[i]):
                ret.append(chr(ord('a') + i))

        return ret
        