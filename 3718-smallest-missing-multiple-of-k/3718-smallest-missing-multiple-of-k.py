class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numbers = set(nums)
        multiple = k

        while multiple in numbers:
            multiple += k

        return multiple