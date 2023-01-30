class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        5 4 1 2
        1 2 4 5
        """
        people.sort()
        left = 0
        count = 0
        num = 0
        right = len(people)-1
        while left < right:
            # print(left,right)
            if people[left] + people[right] <= limit:
                count += 1
                num += 2
                left += 1
                right -= 1
            else:
                right -=1 
            
        count += len(people)-num
        
        return count
