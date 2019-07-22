class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])

    def spiral_helper(result, offset, matrix):
        if len(matrix[0] == 1):
            return False
