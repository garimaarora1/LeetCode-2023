class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        low, high = 0, (row*col)-1
        
        while low <= high:
            mid = (low + high) // 2
            mid_ele = matrix[mid // col][mid % col]
            if target == mid_ele:
                return True
            elif target < mid_ele:
                high = mid - 1
            else:
                low = mid + 1
        return False