class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort nums
        de-dup at first element
        de-dup at second element
        """
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            goal = - nums[i]
            
            first = i+1
            second = n-1
    
            while first < second:
                curr_sum = nums[first] + nums[second]
                
                if curr_sum == goal:
                    ans.append([nums[i], nums[first], nums[second]])
                    
                    first += 1
                    second -= 1
                    
                    while first < second and nums[first] == nums[first-1]:
                        first += 1
                elif curr_sum < goal:
                    first += 1
                else:
                    second -= 1
        return ans