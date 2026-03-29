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
        # sub boxes are [0-2] x [0-2]
        # key : sub_box (row // 3, column // 3)
        # value : set of numbers in sub_box
        sub_boxes = {
            (i, j): set() for i in range(3) for j in range(3)
        }

        # encode all numbers into sub_boxes
        for row in range(len(board)):
            for column in range(len(board)):
                sub_box = sub_boxes[(row // 3, column // 3)]
                element = board[row][column]
                if element in sub_box and element != ".":
                    return False
                sub_box.add(element)
            
        
        # if board passes all tests
        return True


# time complexity if the sudoku grid were unbounded: O(n^2)
# space complexity: O(n)
