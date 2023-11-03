class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        def binary_search(arr):
            lo, hi = 0, len(arr)-1
            while lo <= hi:
                mid = lo + (hi-lo)//2
                if arr[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return len(arr) - lo
                

        row = len(grid)
        for row in grid:
            ans += binary_search(row)
        return ans

        
        
        
    
        