class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, len(nums)-1
        c = 0
        while c<=p2:
            if nums[c] == 0:
                nums[c], nums[p1] = nums[p1],nums[c]
                p1 += 1
                c += 1
            elif nums[c] == 2:
                nums[c], nums[p2] = nums[p2],nums[c]
                p2 -= 1
            else:
                c += 1