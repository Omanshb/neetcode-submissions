class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        internal = -1
        while l <= r:
            middle = (l + r) // 2
            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                internal = middle
                break
            elif target < matrix[middle][0]:
                r = middle - 1
            else:
                l = middle + 1
        if internal == -1:
            return False
        
        l, r = 0, len(matrix[0])
        while l <= r:
            middle = (l + r) // 2
            if target < matrix[internal][middle]:
                r = middle - 1
            elif target > matrix[internal][middle]:
                l = middle + 1
            else:
                return True
        return False

        