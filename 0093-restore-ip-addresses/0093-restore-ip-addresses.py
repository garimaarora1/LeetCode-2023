class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        
        def dfs(i, parts):
            # Base case: If there are more than 4 parts, return
            if len(parts) > 4:
                return
            
            # Base case: If end of string and exactly 4 parts, add to result
            if i == n and len(parts) == 4:
                ans.append('.'.join(parts))
                return
            
            # Try each possible part length (1 to 3 characters)
            for j in range(i, min(i+3, n)):
                part = s[i: j+1]
                
                # Skip invalid parts
                if len(part) > 1 and part[0] == '0':
                    continue
                if len(part) >= 4 or int(part) > 255:
                    continue
                # Add part and recurse
                parts.append(part)
                dfs(j+1, parts)
                parts.pop()
        
        dfs(0, [])
        return ans
