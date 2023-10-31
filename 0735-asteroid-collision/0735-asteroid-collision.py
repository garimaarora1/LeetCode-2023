class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            if not st:
                st.append(asteroid)
            else:
                # append negatives -1 -1 -100
                if st[-1] < 0 and asteroid < 0:
                    st.append(asteroid)
                
                # append positives 1 2 3 5 500
                elif st[-1] > 0 and asteroid > 0:
                    st.append(asteroid)
                
                # collision when st[-1] is negative
                elif st and st[-1] > 0 and asteroid < 0:
                    while ((st and st[-1] >0 and st[-1] < abs(asteroid))):
                        st.pop()
                    if st and st[-1] == abs(asteroid):
                        st.pop()
                    elif (st and st[-1] < 0) or not st:
                        st.append(asteroid)
                    # if abs(asteroid)
                    # st.append(asteroid)
                else:
                    st.append(asteroid)
        return st
    

        