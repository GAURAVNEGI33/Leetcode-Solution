class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Option 1: Buy type 1 and type 2 items separately
        separate = need1 * cost1 + need2 * cost2

        # Option 2: Buy type 3 items for the common requirement
        both = min(need1, need2) * costBoth

        # Remaining requirements are fulfilled separately
        both += max(0, need1 - need2) * cost1
        both += max(0, need2 - need1) * cost2

        # Option 3: Buy type 3 items even for the extra requirement
        extra = max(need1, need2) * costBoth

        return min(separate, both, extra)