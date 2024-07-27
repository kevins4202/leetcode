class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]

        year = int(date[:4])

        month = int(date[5:7])

        day = int(date[-2:])

        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0): days[1] = 29

        ans = sum(days[:month - 1])

        return ans + day