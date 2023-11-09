class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0,0)] for i in range(length)]
        self.sn = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.sn,val))

    def snap(self) -> int:
        self.sn += 1
        return self.sn -1 

    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        left,right = 0,len(arr)-1

        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid][0] > snap_id:
                right = mid - 1
            else:
                left = mid + 1
        
        return arr[right][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)