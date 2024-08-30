
class Solution:
    """
    This indicates that if we can somehow "divide" a range of numbers into segments proportional to the weights, we could pick a random number within that range and determine which segment it falls into.
    """
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total_sum = 0
        for weight in w:
            self.total_sum += weight
            self.prefix_sum.append(self.total_sum)

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        for i, curr_prefix_sum in enumerate(self.prefix_sum):
            if target <= curr_prefix_sum:
                return i
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()