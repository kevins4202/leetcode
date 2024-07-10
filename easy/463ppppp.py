class Solution:
    

        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        bfs = []

        x = 0
        y = 0

        ok = False
        while x < rows:
            y = 0
            
            while y < cols:
                if grid[x][y]:
                    ok = True
                    break
                y+=1

            if ok:
                break
            
            x+=1

        print(f'{x} {y}')

        grid[x][y] = 2
        
        bfs.append((x,y))

        ans = 0
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        while len(bfs):
            curr = bfs.pop()

            x = curr[0]
            y = curr[1]

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if xx < 0 or xx >= rows or yy < 0 or yy >= cols or grid[xx][yy] == 0:
                    ans+=1
                elif grid[xx][yy] == 1:
                    grid[xx][yy] = 2
                    bfs.append((xx,yy))

        return ans

# def islandPerimeter(grid: List[List[int]]) -> int:
#     perimeter = 0
    
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == 1:
#                 perimeter += 4
#                 if i > 0 and grid[i - 1][j] == 1:
#                     perimeter -= 2
#                 if j > 0 and grid[i][j - 1] == 1:
#                     perimeter -= 2
    
#     return perimeter