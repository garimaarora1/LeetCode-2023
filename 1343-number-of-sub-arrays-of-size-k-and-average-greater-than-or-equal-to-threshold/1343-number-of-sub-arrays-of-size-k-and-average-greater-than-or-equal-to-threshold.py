class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = j = 0
        curr_sum = 0
        count = 0
        while j < len(arr):
            curr_sum += arr[j]

            if j-i+1 == k:
                if (curr_sum / k )>= threshold:
                    count += 1
                curr_sum -= arr[i]
                i += 1
            j += 1
        return count