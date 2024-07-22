def addToArrayForm(num: List[int], k: int) -> List[int]:
    i = len(num) - 1
    carry = 0
    while k or carry > 0:
        if i < 0:
            i = 0
            num.insert(i, 0)
        temp = num[i] + carry + k % 10
        carry = temp // 10
        num[i] = temp % 10
        # print(temp)
        k //= 10
        i -= 1
    return num