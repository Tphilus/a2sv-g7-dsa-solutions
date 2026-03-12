class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()   
        left = 0
        right = len(skill) - 1

        total_sum = skill[left] + skill[right]
        total_chemistry = 0

        while left < right:
            curr_sum = skill[left] + skill[right]

            if curr_sum != total_sum:
                return -1
           
            total_chemistry += (skill[left] * skill[right])

            left += 1
            right -= 1

        return total_chemistry