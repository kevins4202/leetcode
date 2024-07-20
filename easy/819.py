class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        
        punc = "!?',;."

        for c in punc: paragraph = paragraph.replace(c, ' ')

        paragraph = [w for w in paragraph.lower().split(' ') if w]

        print(paragraph)

        cnt = dict()

        for w in paragraph:
            if w not in cnt and w not in ban:
                cnt[w] = 0
            
            if w not in ban:
                # print(w)
                cnt[w] += 1

        return max(cnt, key = cnt.get)
