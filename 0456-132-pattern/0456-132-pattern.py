class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = nums[0]
        mono_st = []
        for num in nums:
            while mono_st and mono_st[-1][0] <= num:
                mono_st.pop()
            
            if mono_st and mono_st[-1][0] > num and mono_st[-1][1] < num:
                return True
            mono_st.append((num,mini))
            mini = min(mini, num)
        return False
        