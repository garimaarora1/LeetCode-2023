class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        queue = deque()
        count = 0
        while j <= len(nums) - 1:
            if nums[j] % 2 == 1:
                queue.append(j)

            while len(queue) > k:
                if nums[i] % 2 == 1:
                    queue.popleft()
                i += 1

            if len(queue) == k:
                count += queue[0] - i + 1
            j += 1

        return count