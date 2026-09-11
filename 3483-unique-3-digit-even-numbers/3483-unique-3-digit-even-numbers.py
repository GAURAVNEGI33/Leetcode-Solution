from itertools import permutations
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                seen.add(perm)
        return len(seen)