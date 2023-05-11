class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        heapq.heapify(arr)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heapq.heappush(arr,matrix[row][col])
        
        
        for i in range(k):
            val = heapq.heappop(arr)
        
        return val