class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        def rec(index,arr):
            if index == 1:
                return [1,1]
            
            val = rec(index-1,arr)
            arr.append(val)
            arr = [0] * (len(val)-1)
            for i in range(len(arr)):
                arr[i] = val[i] + val[i+1] 
            
            return [1] + arr + [1]
        rec(numRows,arr)
        return arr