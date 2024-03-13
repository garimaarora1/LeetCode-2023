class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, maxi = 0, len(height)-1, 0
        while i < j:
            area = (j-i) * min(height[i], height[j])
            maxi = max(maxi, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi
        