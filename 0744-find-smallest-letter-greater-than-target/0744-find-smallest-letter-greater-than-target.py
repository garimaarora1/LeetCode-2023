class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mini = letters[0]
        lo, hi = 0, len(letters)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if letters[mid] > target:
                print("mini:", mini)
                print("letters[mid]:", letters[mid])
                if mini <= target:
                    print(1)
                    mini = letters[mid]
                else:
                    mini = min(mini, letters[mid])
                print("final_mini:", mini)
                hi = mid - 1
            else:
                lo = mid + 1
        return mini

        