class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp = 0
        act=0

        n = len(nums)
        exp = n*(n+1)//2
        act = sum(nums)

        return exp-act
      

