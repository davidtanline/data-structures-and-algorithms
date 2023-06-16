'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. 
The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
'''

from typing import List

def island_perimeter(grid: List[List[int]]) -> int:
        R = len(grid) - 1
        C = len(grid[0]) - 1
        perimeter = 0

        for i in range(0, R + 1):
            for j in range(0, C + 1):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    if i == R or grid[i + 1][j] == 0:
                        perimeter += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    if j == C or grid[i][j + 1] == 0:
                        perimeter += 1
        
        return perimeter

# tests
print("Case 1 --- Expected: 16, Actual: ", island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print("Case 2 --- Expected: 4, Actual: ", island_perimeter([[1]]))
print("Case 3 --- Expected: 4, Actual: ", island_perimeter([[1,0]]))