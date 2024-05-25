from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0,0
        d = deque()
        ans = []
        while j < len(nums):
            while d and d[-1]<nums[j]:
                d.pop()
            d.append(nums[j])
            if j-i+1 == k:
                ans.append(d[0])
                if nums[i]==d[0]:
                    d.popleft()
                i += 1
            j += 1
        return ans