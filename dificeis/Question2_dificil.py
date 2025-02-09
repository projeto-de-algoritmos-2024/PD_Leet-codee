class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        total = 0
        max_satisfaction = 0

        for i in range(len(satisfaction) - 1, -1, -1):
            total += satisfaction[i]
            
            if total + max_satisfaction <= max_satisfaction:
                break
            
            max_satisfaction += total
        
        return max_satisfaction