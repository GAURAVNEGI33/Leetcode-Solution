class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        write = 0

        for num in nums:
            if num  not in seen:
                seen.add(num)
                nums[write]=num
                write+=1
        return write 
