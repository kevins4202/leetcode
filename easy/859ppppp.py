class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False

        if s == goal:
            for x in 'qwertyuiopasdfghjklzxcvbnm':
                if s.count(x) >= 2: return True
            return False

        indexes = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                indexes.append(i)
        
        return len(indexes) == 2 and s[indexes[0]] == goal[indexes[1]] and s[indexes[1]] == goal[indexes[0]]