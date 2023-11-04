class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return 

        # result array, contain values "Push", "Pop"
        res = []
        st = []
        stream = 1
        i = 0

        while i < len(target):
            while not st or (st and st[-1]+1 < target[i]):
                st.append(stream)
                res.append("Push")
                stream += 1

            while st and st[-1] < target[i] and (st[-1] > target[i-1] or i == 0):
                st.pop()
                res.append("Pop")
            
            if st == target:
                return res

            st.append(stream)
            stream += 1
            res.append("Push")
            i += 1
        return res
    
    
