class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.Counter(deck)

        if len(deck) ==1 :return False

        ks = list(counter.values())
        gc = ks[-1]


        for x in ks[:-1]:
            gc = gcd(gc, x)


            if gc == 1: return False

        return True