class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        output = 0

        for i in range(N):
            output += mat[i][i]
            output += mat[N - 1 - i][i]

        if N % 2 != 0:
            output -= mat[N // 2][N // 2]
        
        return output
            
