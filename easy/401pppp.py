class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    ret.append(f'{h}:{m:02d}')
        
        return ret

        