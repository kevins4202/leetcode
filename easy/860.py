class Solution:
    def lemonadeChange(self, s: List[int]) -> bool:
        bills = dict()

        bills[5] = 0
        bills[10] = 0

        for x in s:
            if x == 5:
                bills[x] += 1
            elif x == 10:
                if bills[5] == 0: return False
                else: bills[5] -= 1
                bills[10] += 1
            elif x == 20:
                if bills[10] == 0:
                    if bills[5] < 3: return False
                    else: bills[5] -= 3
                else:
                    if bills[5] == 0: return False
                    else: 
                        bills[5] -= 1
                        bills[10] -=1
        
        return True
                