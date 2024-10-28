class Solution:
    """        
    Steps:
    1. Add the new window element to the queue, ensuring it stays monotonically decreasing.
    2. Add the first element of the queue to the answer on each new window hit.
    3. Remove the element from the front of the queue if the window no longer contains it.
        Note: For this reason we will be storing indexes in queue and not the elements.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        queue = deque() # indexes, monotonically decreasing
        i = j = 0
        
        while j < len(nums):
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)
            
            if j - i + 1 == k:
                answer.append(nums[queue[0]])
                i += 1
                
                if i > queue[0]:
                    queue.popleft()
            j += 1
        return answer
                
