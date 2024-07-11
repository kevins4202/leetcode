class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = list(enumerate(score))

        scores = sorted(scores, key = lambda tup: tup[1], reverse = True)

        ans = [0] * len(score)

        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for i, tup in enumerate(scores):
            ans[tup[0]] = medal[i] if i < 3 else str(i+1)

        return ans

