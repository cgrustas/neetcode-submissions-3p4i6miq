class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for duplicates in rows
        for row in board: 
            row_set = set()
            for element in row:
                if element in row_set and element != ".":
                        return False
                row_set.add(element)

        # look for duplicates in columns
        for i in range(len(board)): 
            column = set()
            for row in board: 
                if row[i] in column and row[i] != ".":
                    return False
                column.add(row[i])

        # look for duplicates in 3x3 sub-boxes
        for i in range(0, 9, 3): 
            for j in range(0, 9, 3): 
                sub_box = set()
                for row in range(i, i + 3): 
                    for column in range(j, j + 3):
                        if board[row][column] in sub_box and board[row][column] != ".":
                            return False
                        sub_box.add(board[row][column])

        return True

# time complexity if the sudoku grid were unbounded: O(n^2)
# space complexity: O(n)
