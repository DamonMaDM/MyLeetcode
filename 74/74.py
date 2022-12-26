class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n= len(matrix[0])
        l = 0
        r = m*n-1
        while l<=r:
            middle = (l+r)//2
            i = middle//n
            j = middle%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = middle+1
            else:
                r = middle-1
        return False