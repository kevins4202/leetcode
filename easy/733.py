class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        queue = [[sr, sc]]

        # for i in range(10):
            # print(len(queue))
        # while len(queue) > 0:
        while True:
            if len(queue) == 0: return image
            curr = queue.pop()
            print(curr)
            image[curr[0]][curr[1]] = color

            for i in range(4):
                xx = curr[0] + dx[i]
                yy = curr[1] + dy[i]

                if xx < 0 or yy < 0 or xx >= len(image) or yy >= len(image[0]) or image[xx][yy] != old:
                    continue
                queue.append([xx, yy])
        
        return image