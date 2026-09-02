class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        # I could simply return True, but I constructed nums2 to demonstrate my approach.
        odd_number = None

        for num in nums1:
            if num % 2 == 1:
                odd_number = num
                break

        nums2 = []

        if odd_number is None:
            nums2 = nums1[:]
        else:
            for num in nums1:
                if num % 2 == 1:
                    nums2.append(num)
                else:
                    nums2.append(num - odd_number)

        parity = nums2[0] % 2

        for num in nums2:
            if num % 2 != parity:
                return False

        return True