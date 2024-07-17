class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # letters = list(set(letters))
        lo = 0
        hi = len(letters) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            print(mid)

            if target[0] < letters[mid][0]:
                hi = mid - 1
            else: lo = mid + 1

        return letters[0] if lo == len(letters) else letters[lo]