class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i == k:
                count += tickets[k]
            elif i <= k and tickets[i] >= tickets[k]:
                
                count += tickets[k]
            
            elif i > k and tickets[i] >= tickets[k]:
                
                count += tickets[k] - 1
            
            elif tickets[i] < tickets[k]:
                
                count += tickets[i]
            
    
        return count