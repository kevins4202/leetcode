class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # list1 = set(list1)
        # list2 = set(list2)
        ans = -1
        ret = []

        l2 = {w: i for i, w in enumerate(list2)}

        for i,w in enumerate(list1):
            if w in l2:
                curr = i + l2[w]
                if ans == curr:
                    ret.append(w)
                elif curr < ans or ans == -1:
                    ret = [w]
                    ans = curr
                    print(w)
        
        return ret