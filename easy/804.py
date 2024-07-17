class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        trans = set()

        for word in words:
            s = ""
            for c in word:
                s += dic[ord(c) - ord ('a')]
            trans.add(s)
        
        return len(trans)