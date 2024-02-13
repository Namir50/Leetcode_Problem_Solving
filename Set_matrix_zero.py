"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. 
Example: Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]] 
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

      rows = len(matrix)  # Get the number of rows in the matrix
      if rows == 0:
        return  # If the matrix is empty, there's nothing to do

      cols = len(matrix[0])  # Get the number of columns in the matrix

      zero_rows, zero_cols = set(), set()  # Initialize sets to keep track of rows and columns containing zeros
    
    # Step 1: Identify positions of zeros
      for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:  # If the current element is zero
                zero_rows.add(i)  # Add the row index to the set of rows containing zeros
                zero_cols.add(j)  # Add the column index to the set of columns containing zeros
    
    # Step 2: Set entire rows and columns to zeros
      for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:  # If the current element's row or column contains zeros
                matrix[i][j] = 0 * rows  # Set the current element to zero
      
    
    # Step 3: Set entire rows to zeros
      for i in zero_rows:
        matrix[i] = [0] * cols
    
      return matrix  # Return the modified matrix
