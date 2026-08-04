class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=Counter(s)
        count_t=Counter(t)
        if count==count_t:
            return True
        else:
            return False