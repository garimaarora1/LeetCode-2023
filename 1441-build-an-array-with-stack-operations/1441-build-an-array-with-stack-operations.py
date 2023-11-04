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
            if st == target:
                return res

            # while st and st[-1] < target[i] and (st[-1] > target[i-1] or i-1 ==0):
            #     print("popping")
            #     st.pop()
            #     res.append("Pop")
            while not st or (st and st[-1]+1 < target[i]):
                print("pushing", stream)
                st.append(stream)
                res.append("Push")
                stream += 1

            while st and st[-1] < target[i] and (st[-1] > target[i-1] or i == 0):
                print("popping")
                st.pop()
                res.append("Pop")
            
            if st == target:
                return res

            print("push")
            st.append(stream)
            stream += 1
            res.append("Push")
#             if st[-1] < target[i]:
#                 print("pop 1")
#                 st.pop()
#                 res.append("Pop")
            i += 1
        print(st)
        return res
    
    
