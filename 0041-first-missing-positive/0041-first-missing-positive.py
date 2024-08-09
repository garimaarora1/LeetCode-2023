class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        n = len(arr)

        # Step 1: Segregate positive numbers from others
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1

        # Step 2: Operate on the positive part of the array
        arr = arr[j:]
        n = len(arr)
        print(arr)
        # Step 3: Mark the presence of elements
        for i in range(n):
            val = abs(arr[i])
            print(arr[i], val)
            if val - 1 < n and arr[val - 1] > 0:
                arr[val - 1] = -arr[val - 1]

        # Step 4: Find the first positive index
        for i in range(n):
            if arr[i] > 0:
                return i + 1

        return n + 1
