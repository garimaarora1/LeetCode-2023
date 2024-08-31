class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            
            if (mid == 0 or arr[mid-1] < arr[mid]) and (mid == len(arr)-1 or arr[mid] > arr[mid+1]):
                return mid

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                # Otherwise, the peak is to the left
                high = mid - 1