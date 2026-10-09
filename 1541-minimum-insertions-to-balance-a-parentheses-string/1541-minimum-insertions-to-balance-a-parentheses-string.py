class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0     # insertions
        need = 0    # number of ')' still required

        for c in s:
            if c == '(':
                # agar need odd hai, ek ')' insert karke pair complete karo
                if need % 2 == 1:
                    ans += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need == -1:
                    # koi '(' nahi mila, '(' insert karo
                    ans += 1
                    need = 1   # us '(' ko ek aur ')' chahiye

        return ans + need