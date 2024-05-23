class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        counter = defaultdict(int)
        while j < len(nums):
            counter[nums[j]] += 1
            if counter[nums[j]] == 2:
                return True
            
            if j-i == k:
                counter[nums[i]] -=1
                i += 1
            j += 1
        return False
                
                
                
            
        