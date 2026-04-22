class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        
        while left <= right:
            middle = (left + right) // 2
            print(middle, middle // len(matrix[0]), middle % len(matrix[0]))
            value = matrix[middle // len(matrix[0])][middle % len(matrix[0])]

            if value == target:
                return True
            elif value > target:
                right = middle - 1
            elif value < target:
                left = middle + 1
        
        return False