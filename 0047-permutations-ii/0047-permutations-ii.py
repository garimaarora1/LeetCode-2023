class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        # nums.sort()
        
        def dfs(i,res):
            if i==len(nums):
                res.append(nums[:])
                return
            s=set()    
            for j in range(i,len(nums)):
                if nums[j] in s:
                    continue
                s.add(nums[j])    
                nums[i],nums[j]=nums[j],nums[i]
                dfs(i+1,res)   
                nums[i],nums[j]=nums[j],nums[i]    

        dfs(0,res)
        return res