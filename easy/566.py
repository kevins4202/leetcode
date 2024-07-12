class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]): return mat
        b = 0

        ret = [[0] * c] * r

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ret[b // c][b % c] = mat[i][j]

                b += 1
            
        
        return ret