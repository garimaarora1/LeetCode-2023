class Solution:    
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(digits)
        res = []

        # Iterate through possible even 3-digit numbers
        for num in range(100, 1000, 2):  # Only even numbers
            temp_map = counter.copy()
            num_str = str(num)
            valid = True
            
            # Check if the current number can be formed using the digits
            for digit in num_str:
                digit = int(digit)
                if temp_map[digit] > 0:
                    temp_map[digit] -= 1
                else:
                    valid = False
                    break  # If digit is not available, number can't be formed
            
            if valid:
                res.append(num)
        
        return res