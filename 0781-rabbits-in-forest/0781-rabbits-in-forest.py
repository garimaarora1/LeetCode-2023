class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0

        for x, freq in count.items():
            group_size = x + 1
            groups = (freq + x) // group_size  # Calculate number of groups
            total_rabbits += groups * group_size

        return total_rabbits