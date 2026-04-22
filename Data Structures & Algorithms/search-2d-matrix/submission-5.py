class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        
        while left <= right:
            middle = (left + right) // 2
            value = matrix[middle // len(matrix[0])][middle % len(matrix[0])]

            if value == target:
                return True
            elif value > target:
                right = middle - 1
            elif value < target:
                left = middle + 1
        
        return False

"""
Intuition: Just binary search again except this time, you just have to properly check
the true middle of the matrix by doing matrix[middle // len(matrix[0])][middle % len(matrix[0])].

Time Complexity: O(n * m) because it's just binary search.

Space Complexity: O(1) because we just hold left, middle, and right values.
"""