class Solution: 
    def select(self, arr, i):
        # code here
        return i
    
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(n):
            min_idx = self.select(arr,i)
            for j in range(i + 1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
