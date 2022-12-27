class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = float('inf')
        answer = -1
        for key,cord in enumerate(points):
            if cord[0] == x or cord[1] == y:
                distance = abs(x-cord[0]) + abs(y-cord[1])
                print(distance)
                if distance < ans:
                    ans = distance
                    answer = key
                
        return answer
