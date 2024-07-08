class Solution:
    def firstUniqChar(self, s: str) -> int:
        text = 'abcdefghijklmnopqrstuvwxyz'
        idx = 100000

        for i in text:

            x = s.find(i)

            if x != -1 and s.rfind(i) == x:
                idx = min(idx, x)

        return idx if idx != 100000 else -1