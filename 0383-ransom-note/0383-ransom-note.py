class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fre ={}
        for char in  magazine :
            fre[char]= fre.get(char,0)+1
        for char in ransomNote:
            if char not in fre or fre[char] == 0:
                return False
            fre[char]-=1
        return True

