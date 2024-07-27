class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)

        cnts = sorted(counter.values())
        for i in range(1, len(cnts)):
            if cnts[i] == cnts[i-1]: return False

        return True
