class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        # 1. hasmap to keep track of freq of each 'int'
        #     res = ''
        #     mid = ''
        # 2. reverse sort the map  -- O(1)
        # 3. condition %2  freq =0 other freq = 1
        # 4. condition >=1 
        # 5. return res + mid + res[::-1]
    
    
        counter = defaultdict(int)
        res, mid = '', ''
        for n in num:
            counter[n] += 1
        sorted_keys = sorted(list(counter.keys()), reverse = True)
        print(sorted_keys)
        for key in sorted_keys:
            res = res + ((key)*((counter[key])//2))
            counter[key] = counter[key]%2
            if counter[key] >=1 and not mid:
                mid = key
        res = res + mid + res[::-1]
        res = res.strip("0")
        return res if res else "0"
            
    