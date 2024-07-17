class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        x = ''.join([str(i) for i in bits])

        queue = [x]

        while queue:
            curr = queue.pop()
            if curr == "": continue

            if curr == "0": return True

            if curr[:2] == "10" or curr[:2] == "11":
                queue.append(curr[2:])
            elif curr[0] == '0': queue.append(curr[1:])

        return False