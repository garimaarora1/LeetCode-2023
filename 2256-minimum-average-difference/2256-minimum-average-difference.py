class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        mini_avg_diff = float('inf')
        i = 0
        n = len(nums)-1
        mini_idx = 0
        for j in range(len(nums)):
            beg_prefix_sum = prefix_sum[j]
            end_prefix_sum = prefix_sum[n] - beg_prefix_sum
            beg_ele_count = j-i+1
            end_ele_count = n - beg_ele_count + 1
            if end_ele_count == 0:
                end_avg = 0
            else:
                end_avg = end_prefix_sum//end_ele_count
            start_avg = beg_prefix_sum//beg_ele_count
            if abs(start_avg - end_avg) < mini_avg_diff:
                mini_avg_diff = min(mini_avg_diff, abs(start_avg - end_avg))
                mini_idx = j
        return mini_idx
                        
        