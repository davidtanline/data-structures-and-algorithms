'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

import collections
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    squareDict = collections.defaultdict(set)
    rowDict = collections.defaultdict(set)
    colDict = collections.defaultdict(set)
    for i in range (0,9):
        for j in range (0,9):
            if board[i][j] != '.':
                if (board[i][j] in rowDict[i]
                    or board[i][j] in colDict[j]
                    or board[i][j] in squareDict[i//3, j//3]
                ):
                    return False
                rowDict[i].add(board[i][j])
                colDict[j].add(board[i][j])
                squareDict[i//3, j//3].add(board[i][j])
    return True

# tests
print("Case 1 --- Expected: True, Actual: ", is_valid_sudoku([["5","3",".",".","7",".",".",".","."]
                                                            ,["6",".",".","1","9","5",".",".","."]
                                                            ,[".","9","8",".",".",".",".","6","."]
                                                            ,["8",".",".",".","6",".",".",".","3"]
                                                            ,["4",".",".","8",".","3",".",".","1"]
                                                            ,["7",".",".",".","2",".",".",".","6"]
                                                            ,[".","6",".",".",".",".","2","8","."]
                                                            ,[".",".",".","4","1","9",".",".","5"]
                                                            ,[".",".",".",".","8",".",".","7","9"]]))
print("Case 2 --- Expected: False, Actual: ", is_valid_sudoku([["8","3",".",".","7",".",".",".","."]
                                                            ,["6",".",".","1","9","5",".",".","."]
                                                            ,[".","9","8",".",".",".",".","6","."]
                                                            ,["8",".",".",".","6",".",".",".","3"]
                                                            ,["4",".",".","8",".","3",".",".","1"]
                                                            ,["7",".",".",".","2",".",".",".","6"]
                                                            ,[".","6",".",".",".",".","2","8","."]
                                                            ,[".",".",".","4","1","9",".",".","5"]
                                                            ,[".",".",".",".","8",".",".","7","9"]]))