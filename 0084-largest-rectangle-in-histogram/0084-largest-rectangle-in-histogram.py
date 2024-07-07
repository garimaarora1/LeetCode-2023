class Solution:
    
    def next_smallest_left(self, heights):
        stack, ans = [], []
        
        for i in range(len(heights)):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1][1])
            else:
                ans.append(-1)
            stack.append((heights[i], i))
        return ans
    
    def next_smallest_right(self, heights):
        stack, ans = [], []
        
        for i in range(len(heights)-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1][1])
            else:
                ans.append(len(heights))
            stack.append((heights[i], i))
        return ans[::-1]

    def largestRectangleArea(self, heights: List[int]) -> int:
        
        l = self.next_smallest_left(heights)
        
        r = self.next_smallest_right(heights)
        
        max_area = -1
        
        for i in range(len(heights)):
            curr_width = r[i] - l[i] - 1
            curr_height = heights[i]
            curr_area = curr_width * curr_height
            max_area = max(max_area, curr_area)
        return max_area
        