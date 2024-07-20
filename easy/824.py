class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        end = "a"

        sentence = sentence.split(' ')

        for i in range(len(sentence)) :
            w = sentence[i]

            if w[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
                w = w[1:] + w[0]
            
            w += "ma" + end

            end += "a"

            sentence[i] = w
        
        return ' '.join(sentence)
