class Solution:

    def merge(self, nums, l, mid, h):
        i, j = l, mid+1
        res = []
        while i<=mid and j<=h:
            if nums[i]<=nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1
        if i<=mid:
            res.extend(nums[i:mid+1])
        if j<=h:
            res.extend(nums[j:h+1])
        nums[l:h+1] = res

    def mergeSort(self, nums, l, h):
        if l>=h: return
        mid = (l+h)//2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid+1, h)
        self.merge(nums, l, mid, h)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
        