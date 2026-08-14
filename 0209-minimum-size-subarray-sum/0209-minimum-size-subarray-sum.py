class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l= 0
        curr_sum = 0
        min_length = float("inf")

        for r in range(len(nums)):
            curr_sum+=nums[r]

            while curr_sum >= target:
                window_len = r - l+1
                min_length= min(min_length, window_len)


                curr_sum-=nums[l]
                l+=1

        if min_length == float("inf"):
            return 0
        return min_length
