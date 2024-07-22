def repeatedNTimes(nums: List[int]) -> int:
    # 1
    # return Counter(nums).most_common(1)[0][0]

    # 2
    arr = set()
    for num in nums:
        if num in arr:
            return num
        else:
            arr.add(num)