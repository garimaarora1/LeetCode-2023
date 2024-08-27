class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        # indexes
        queue = deque() 
        i = j = 0
        while j < len(nums):
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)

            if i > queue[0]:
                queue.popleft()

            if (j + 1) >= k:
                answer.append(nums[queue[0]])
                i += 1
            j += 1

        return answer
