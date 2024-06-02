class Solution:
    def trap(self, height: List[int]) -> int:
        
        # two pointes, left, right, lmax, rmax, ans
        if not height: return 0
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        ans = 0
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                ans += rmax - height[r]
        return ans
        
        