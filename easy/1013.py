def canThreePartsEqualSum(arr: List[int]) -> bool:
    total_sum = sum(arr)
    if total_sum % 3 != 0:
        return False

    target = sum(arr) // 3
    current = 0
    count = 0
    for num in arr:
        current += num
        if current == target:
            count += 1
            current = 0
        if count == 3:
            return True
    return False