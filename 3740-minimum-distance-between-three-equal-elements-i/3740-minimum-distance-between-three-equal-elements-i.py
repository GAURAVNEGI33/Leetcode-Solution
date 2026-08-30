class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        answer = float("inf")

        for index, num in enumerate(nums):
            if num not in positions:
                positions[num] = []

            positions[num].append(index)

            # Is number ki latest 3 occurrences
            if len(positions[num]) >= 3:
                first = positions[num][-3]
                third = positions[num][-1]

                distance = 2 * (third - first)
                answer = min(answer, distance)

        if answer == float("inf"):
            return -1

        return answer