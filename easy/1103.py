class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        give = 1

        i = 0
        ans = [0] * num_people
        while candies >= give:
            # print(ans)
            ans[i] += give

            candies -= give

            give += 1
            i = (i + 1) % num_people

            

        ans[i] += candies

        return ans