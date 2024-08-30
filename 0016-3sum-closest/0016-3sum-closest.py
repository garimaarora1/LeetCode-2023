class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        sort 
        for n
        j i+1 -- de- dup 
        """
        n = len(nums)
        nums.sort()
        min_diff = float('inf')
        min_diff_sum = 0
        
        for i in range(n):
            if i >=1 and nums[i] == nums[i-1]:
                    continue

            first = i + 1
            second = n - 1
            
            while first < second:
                
                curr_sum = nums[first] + nums[second] + nums[i]

                if curr_sum == target:         
                    first += 1
                    second -= 1
                    while first < second and nums[first] == nums[first-1]:
                        first += 1
                        
                elif curr_sum < target:
                    first += 1
                
                else:
                    second -= 1
                curr_diff = abs(target - curr_sum)
                if curr_diff < min_diff:
                    min_diff = curr_diff
                    min_diff_sum = curr_sum
        return min_diff_sum
        