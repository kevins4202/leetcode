class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = []
        num1 = [ord(x) - ord('0') for x in num1]
        num2 = [ord(x) - ord('0') for x in num2]
        carry = 0
        while num1 or num2 or carry:
            x1 = num1.pop() if num1 else 0
            x2 = num2.pop() if num2 else 0
            carry, res = divmod(x1 + x2 + carry, 10)
            ret.append(chr(res + ord('0')))
        return "".join(reversed(ret))