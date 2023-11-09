class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x1, y1 = coordinates[0][0], coordinates[0][1]

        def calcslope(x2,y2):
            return (y2-y1) / (x2-x1) if (x2-x1) != 0 else None

        slope = calcslope(coordinates[1][0], coordinates[1][1])

        for i in range(1,len(coordinates)):  
            if slope != calcslope(coordinates[i][0],coordinates[i][1]): return False
        
        return True

