class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise and hare 
        # Step 1: find the intersection
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break
                        
        # Step 2: find the cycle enterance 

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
        
        