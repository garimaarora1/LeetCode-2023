class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Step 1: split nums in three lists of positives, negatives and zeroes
        p, n, z = [], [], []
        ans = set()
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        
                
        # Step 2: makep positivies and negatives sets for O(1) lookup 
        p_set = set(p)
        n_set = set(n)
        
        # Step-3: if there is atleast 1 zero, check for the case where num and -num also exist
        
        if z:
            for num in p_set:
                if -num in n_set:
                    ans.add((-num, 0, num))
        
        # Step-4: if there are at least 3 zeroes, at (0,0,0) to the answer
        
        if len(z) >= 3:
            ans.add((0,0,0))
            
        # Step-5: for every pair of element in positives, check for the compliment in negatives
        
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -(p[i]+p[j])
                if target in n_set:
                    print("here")
                    ans.add(tuple(sorted([p[i], p[j], target])))
                    
                    
        # Step-6: for every pair of element in negatives, check for the compliment in positives
        
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -(n[i]+n[j])
                if target in p_set:
                    print("here2")
                    ans.add(tuple(sorted([n[i], n[j], target])))
        return ans
            