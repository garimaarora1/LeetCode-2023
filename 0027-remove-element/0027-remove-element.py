class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        kth_index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                if i != kth_index:
                    nums[kth_index] = nums[i]
                kth_index += 1
        return kth_index
        