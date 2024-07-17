class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        curr = 0
        lines = 1
        for c in s:
            index = ord(c) - ord('a')
            
            if curr + widths[index] > 100:
                curr = widths[index]
                lines+=1
            else:
                curr += widths[index]
            
        return [lines, curr]
        