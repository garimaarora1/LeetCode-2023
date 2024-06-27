class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u1,v1 = edges[0]
        
        if u1 in edges[1]:
            return u1
        if v1 in edges[1]:
            return v1
        
        