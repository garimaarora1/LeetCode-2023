
class Solution:
    """
    This indicates that if we can somehow "divide" a range of numbers into segments proportional to the weights, we could pick a random number within that range and determine which segment it falls into.
    """
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total_sum = 0
        self.total_weights = len(w)

        for weight in w:
            self.total_sum += weight
            self.prefix_sum.append(self.total_sum)

    def pickIndex(self) -> int:
        low, high = 0, self.total_weights - 1
        target = random.randint(1, self.total_sum)

        while low <= high:
            mid = (low + high) // 2
            
            if self.prefix_sum[mid] == target:
                return mid
            if self.prefix_sum[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            """If the loop finishes without directly finding the target, low will point to the first index where the cumulative sum is greater than the target, which is the correct index to return."""

        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()