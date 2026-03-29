from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create dictionaries for rows, columns, sub_boxes
        rows = defaultdict(set)
        columns = defaultdict(set)
        sub_boxes = defaultdict(set)

        # iterate through every element in the board
        for row in range(9):
            for col in range(9):
                # skip over null ('.') values
                element = board[row][col]
                if element == '.':
                    continue

                # if element is already in set
                if (element in rows[row] or
                   element in columns[col] or
                   element in sub_boxes[(row // 3, col // 3)]):
                    return False
                
                # else, add to set
                rows[row].add(element)
                columns[col].add(element)
                sub_boxes[(row // 3, col // 3)].add(element)
        
        # if board has no duplicates in each row/column/sub_box
        return True

