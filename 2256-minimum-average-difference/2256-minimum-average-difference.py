class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        curr_prefix_sum = 0
        mini_avg_diff = float('inf')
        n = len(nums)
        mini_idx = 0
        total_sum = sum(nums)
        
        for i in range(len(nums)):
            curr_prefix_sum += nums[i]
            
            
            # Calculate average of left part of array, index 0 to i.
            left_part_average = curr_prefix_sum
            left_part_average //= (i + 1)
            
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = total_sum - curr_prefix_sum
            # If right part have 0 elements, then we don't divide by 0.
            if i != n - 1:
                right_part_average //= (n - i - 1)
                
            abs_diff = abs(left_part_average - right_part_average)
            if abs_diff < mini_avg_diff:
                mini_avg_diff = abs_diff
                mini_idx = i
        return mini_idx
                        
        