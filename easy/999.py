class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        ans = 0
        
        x = 0
        y = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R': 
                    x = i
                    y = j

        for i in range(4):
            bishop = False

            xx = x
            yy = y

            while xx >= 0 and xx < len(board) and yy >= 0 and yy < len(board[0]) and board[xx][yy] != 'p' and board[xx][yy] != 'B':
                xx += dx[i]
                yy += dy[i]

            if xx >= 0 and xx < len(board) and yy >= 0 and yy < len(board[0]) and board[xx][yy] == 'p': ans+=1

        return ans