class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for px, py in list(self.points.keys()):
            if px != x and py != y and abs(px - x) == abs(py - y):
                count += self.points[(px, py)] * self.points[(px, y)] * self.points[(x, py)]

        return count
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)