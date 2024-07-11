class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if(num==1):
            return False
        sum=0
        p=int(math.sqrt(num))
        for i in range(1, int(num**0.5)+1):
            if(num%i==0):
                sum=sum+num//i
                sum=sum+i
        if((sum-num)==num):
            return True
        return False
        