class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direc = [(0,1),(-1,0),(0,-1),(1,0)]
        direction = 0
        def getLeft(index):
            return (index+1) % 4 
        def getRight(index):
            return (index-1) % 4
        start = [0,0]
        for i in range(100):
            for char in instructions:
                if char == "L":
                    direction = getLeft(direction)
                elif char == "R":
                    direction = getRight(direction)
                else:
                    x,y = start
                    moveX,moveY = direc[direction]
                    start = [x+moveX,y+moveY]
        start.append(direction)

        return (0,0,0) == tuple(start)