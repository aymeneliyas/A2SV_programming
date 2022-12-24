class Solution:
    def average(self, salary: List[int]) -> float:
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        print(salary)
        
        sum = 0
        for i in range(1,len(salary)-1):
            
            sum += salary[i]
        ans = sum / (len(salary)-2)
        
        return ans
