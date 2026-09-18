class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = 0
        result =[]
        for num in nums:
            prefix += num
            result.append(prefix)
        return result
