class Solution:
    def largestNumber(self, nums: List[int]) -> str:
         
        def cmp_func(x, y):
            if x + y > y + x:
                return 1
            return -1
            
        nums = [str(num) for num in nums]
        
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)
        
        return ''.join(nums).lstrip('0') or '0'