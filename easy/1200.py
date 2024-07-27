class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)

        ans = []
        mini = 10000000

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < mini:
                ans = [[arr[i-1], arr[i]]]
                mini = arr[i] - arr[i-1]
            elif arr[i] - arr[i-1] == mini:
                ans.append([arr[i-1], arr[i]])

        return ans