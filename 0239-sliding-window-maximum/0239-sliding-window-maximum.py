class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = j = 0
        deq = deque()
        res = []
        while j < len(nums):
            while deq and deq[-1] < nums[j]:
                deq.pop()
            deq.append(nums[j])
            if j-i+1 == k:
                res.append(deq[0])
                if nums[i] == deq[0]:
                    deq.popleft()
                i += 1
            j += 1
            
        return res