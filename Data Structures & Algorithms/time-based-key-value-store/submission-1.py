class TimeMap:

    def __init__(self):
        self.seen=dict() # valus are list where each element is a 2d element list {alice: [[1, happy], [2,sad]]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.seen:
            self.seen[key].append([timestamp, value])
        else:
            self.seen[key]=[[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.seen:
            return ""
        else:
            arr=self.seen[key]
            low=0
            high=len(arr)-1
            potential=-1
            while low<=high:
                mid=int((low+high)/2)
                if arr[mid][0]==timestamp:
                    return arr[mid][1]
                elif arr[mid][0]<timestamp:
                    low=mid+1
                    potential=mid
                elif arr[mid][0]>timestamp:
                    high=mid-1
            if potential==-1:
                return ""
            else:
                return arr[potential][1]


        
