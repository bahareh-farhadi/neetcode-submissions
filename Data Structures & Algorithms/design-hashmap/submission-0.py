class MyHashMap:

    def __init__(self):
        self.my_hash=list()
        for i in range(1000000+2):
            self.my_hash.append(-1)
        

    def put(self, key: int, value: int) -> None:
        self.my_hash[key]=value
        

    def get(self, key: int) -> int:
        return self.my_hash[key]
        

    def remove(self, key: int) -> None:
        self.my_hash[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)