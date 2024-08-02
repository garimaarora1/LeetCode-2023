class Solution:
    def minSwaps(self, a: List[int]) -> int:
        no_of_ones=a.count(1)
        a=a+a
        ones_in_window,max_ones_in_window=0,0
        for i in range(len(a)):
            if a[i]:
                ones_in_window+=1
            if i>=no_of_ones and a[i-no_of_ones]:
                ones_in_window-=1
            max_ones_in_window=max(ones_in_window,max_ones_in_window)
        return no_of_ones - max_ones_in_window