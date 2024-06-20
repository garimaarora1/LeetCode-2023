class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        
        # A valid IP address must be in the form of A.B.C.D, 
        # where A,B,C and D are numbers from 0-255. 
        # The numbers cannot be 0 prefixed unless they are 0.
        def solve(section,idx):
            if len(section) == 4:
                if idx >= len(s):
                    address = ".".join(section)
                    solutions.append(address)
                return
            for i in range(idx,min(len(s),idx+3)):
                curr = s[idx:i+1]
                if curr[0] == '0' and len(curr) > 1:
                    continue
                if int(curr) >= 0 and int(curr) <= 255:
                    solve(section+[curr],i+1) 
        solutions = []
        solve([],0)
        return solutions