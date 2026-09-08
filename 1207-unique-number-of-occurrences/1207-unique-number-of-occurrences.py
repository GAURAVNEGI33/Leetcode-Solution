class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        fre = {}

        for num in arr:
            fre[num] = fre.get(num,0)+1

        occ = fre.values()
        return len(occ)== len(set(occ))