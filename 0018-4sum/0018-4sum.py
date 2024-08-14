class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, n):
                
                goal = target - nums[i] - nums[j]
                
                start = j + 1
                end = n - 1
                
                while start < end:
                    curr_sum = nums[start] + nums[end]
                    if curr_sum == goal:
                        ans.append((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                        
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif curr_sum < goal:
                        start += 1
                    else:
                        end -= 1
        return set(ans)
                        
                
                
                
                