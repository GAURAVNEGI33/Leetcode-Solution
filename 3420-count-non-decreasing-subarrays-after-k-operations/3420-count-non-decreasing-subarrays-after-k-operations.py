from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Step 1: Next Greater Element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Step 2: Prefix Sum
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Step 3: Binary Lifting
        LOG = n.bit_length()

        jump = [[n] * (n + 1) for _ in range(LOG)]
        cost = [[0] * (n + 1) for _ in range(LOG)]

        for i in range(n):
            jump[0][i] = nxt[i]
            cost[0][i] = nums[i] * (nxt[i] - i)

        for j in range(1, LOG):
            for i in range(n):
                mid = jump[j - 1][i]

                jump[j][i] = jump[j - 1][mid]
                cost[j][i] = cost[j - 1][i] + cost[j - 1][mid]

        # Step 4: Calculate operations required
        def get_cost(l, r):
            total = 0
            cur = l

            for j in range(LOG - 1, -1, -1):
                nxt_pos = jump[j][cur]

                if nxt_pos <= r:
                    total += cost[j][cur]
                    cur = nxt_pos

            total += nums[cur] * (r - cur + 1)

            return total - (pref[r + 1] - pref[l])

        # Step 5: Sliding Window
        ans = 0
        left = 0

        for right in range(n):

            while get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans