class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        def greater_than_target(value) -> bool:
            return value > target
        
        outer_left, outer_right = 0, len(matrix)
        while outer_left < outer_right:
            outer_mid = (outer_left + outer_right) // 2
            inner_left, inner_right = 0, len(matrix[0])

            while inner_left < inner_right:
                inner_mid = (inner_left + inner_right) // 2

                if matrix[outer_mid][inner_mid] == target:
                    return True
                elif greater_than_target(matrix[outer_mid][inner_mid]):
                    inner_right = inner_mid
                else:
                    inner_left = inner_mid + 1
            
            if greater_than_target(matrix[outer_mid][inner_left - 1]):
                outer_right = outer_mid
            else:
                outer_left = outer_mid + 1

        return False
            
        
