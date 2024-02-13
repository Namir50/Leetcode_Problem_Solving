"""Given an m x n matrix, return all elements of the matrix in spiral order
Example 1: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2: Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7] """

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      if not matrix:
        return []

      rows, cols = len(matrix), len(matrix[0])
      top, bottom, left, right = 0, rows - 1, 0, cols - 1
      result = []

      while top <= bottom and left <= right:
        # Traverse top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse rightmost column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse leftmost column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

      return result
