class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # binary search
        left = 0
        right = m * n - 1
        while left <= right:
            middle = (left + right) // 2
            # key part: get indices for 2d non-jagged array from 1d index
            i, j = middle // n, middle % n
            if target < matrix[i][j]:
                right = middle - 1
            elif target > matrix[i][j]:
                left = middle + 1
            else:
                return True
        return False
