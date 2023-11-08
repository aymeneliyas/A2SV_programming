from sortedcontainers import SortedSet
class TimeMap:

    def __init__(self):
        self.arr = defaultdict(SortedSet)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].add((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_right(self.arr[key],(timestamp,chr(127)))
        if key not in self.arr or index == 0:
            return ""
        
        return self.arr[key][index-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)