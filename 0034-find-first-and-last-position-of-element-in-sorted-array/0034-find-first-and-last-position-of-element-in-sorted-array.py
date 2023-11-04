class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
        
        def left(a, target, start, end):
            res = -1
            while start <= end:
                mid = (end+start)//2
                if target == a[mid]:
                    res = mid 
                    end = mid-1
                elif target < a[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return res
        
        def right(a, target, start, end):
            res = -1
            while start <= end:
                mid = (end+start)//2
                if target == a[mid]:
                    res = mid 
                    start = mid+1
                elif target < a[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return res
        
        if len(a)==0:
            return -1,-1
        
        l = left(a, target, 0, len(a)-1)
        r = right(a, target, l, len(a)-1)
        
        return l,r