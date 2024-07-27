class Solution:
    def numEquivDominoPairs(self, dom: List[List[int]]) -> int:
        cache = defaultdict(int)
        for a, b in dom:
            pair = [b,a] if a > b else [a,b]
            cache[tuple(pair)] += 1
        
        return sum([v * (v - 1) // 2 for v in cache.values()])