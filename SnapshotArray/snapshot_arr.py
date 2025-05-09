class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snap_id = 0
        self.snapshots = [0]
        self.array = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if index < self.length:
            self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        self.snapshots.append(self.snap_id)
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id < len(self.snapshots) and index < self.length:
            ret = None
            for sid, val in self.array[index]:
                if sid > snap_id:
                    break
                ret = val
            return ret

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
