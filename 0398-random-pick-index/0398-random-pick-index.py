class Solution:

    def __init__(self, nums: List[int]):
        self.indices_map = defaultdict(list)
        
        
        for i, num in enumerate(nums):
            self.indices_map[num].append(i)
        

    def pick(self, target: int) -> int:
        num_indices = self.indices_map[target]
        return random.choice(num_indices) 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)