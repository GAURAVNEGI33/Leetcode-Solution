class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        n = len(nums)
        exp = n*(n+1)//2
        act = sum(nums)

        return exp-act
      

