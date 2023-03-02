class Solution:
    def winner(self,arr,left,right,turn):
        if left == right:
            if turn:
                return [arr[left],0]
            else:
                return [0,arr[left]]
        
        if turn:
            l = self.winner(arr,left+1,right,not turn)
            r = self.winner(arr,left,right-1,not turn)
            
    
            l[0] += arr[left]
            r[0] += arr[right]
            
            if l[0] > r[0]:
                return l
            else:
                return r
        
        if not turn:
            l = self.winner(arr,left+1,right,not turn)
            r = self.winner(arr,left,right-1,not turn)

            l[1] += arr[left]
            r[1] += arr[right]

            if l[1] > r[1]:
                return l
            else:
                return r

            
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.winner(nums,0,len(nums)-1,True)
        if score[0] >= score[1]:
            return True
        return False