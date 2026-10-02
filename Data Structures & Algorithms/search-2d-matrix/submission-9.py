class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False


        # row = 0
        # left, right = 0, len(matrix)-1
        # while left <= right:
        #     mid = (left + right)//2
        #     if matrix[mid][0] > target:
        #         right = mid - 1
        #     elif matrix[mid][-1] < target:
        #         left = mid + 1
        #     else:
        #         row = mid
        #         break

        # if not left <= right:
        #     return False
    
        # l, r = 0, len(matrix[row])-1
        # while l <= r:
        #     mid = (l + r)//2
        #     if matrix[row][mid] < target:
        #         l = mid + 1
        #     elif matrix[row][mid] > target:
        #         r = mid - 1
        #     else:
        #         return True
        
        # return False
        

        