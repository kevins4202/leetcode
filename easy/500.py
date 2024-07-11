class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        def can_type(word, row):
            return all(c.lower() in row for c in word)
        
        ans = []
        for word in words:
            if can_type(word, row1) or can_type(word, row2) or can_type(word, row3):
                ans.append(word)
        return ans