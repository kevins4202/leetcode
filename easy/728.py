class Solution:
    def slf(self, x):
        n = x
        while n:
            if n % 10 == 0 or x % (n % 10) != 0: return False
            n //= 10
        
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if self.slf(x)]