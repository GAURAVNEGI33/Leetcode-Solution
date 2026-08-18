class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        fre = {}
        max_l = 0

        for r in range(len(fruits)):
            right_fruit = fruits[r]
            left_fruit = fruits[l]

            fre[right_fruit] = fre.get(right_fruit,0)+1

            while len(fre)>2:
                left_fruit = fruits[l]
                fre[left_fruit] -= 1


                if fre[left_fruit] == 0:
                    del fre[left_fruit]

                l+=1

            win_l = r - l+1
            max_l= max(max_l, win_l)
        return max_l

         

