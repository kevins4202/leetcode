class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order2 = {arr2[i] : i for i in range(len(arr2))}

        tmp1, tmp2 = [], []

        for x in arr1:
            if x in order2: tmp1.append(x)
            else: tmp2.append(x)

        return sorted(tmp1, key = lambda x: order2[x]) + sorted(tmp2)