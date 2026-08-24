class MyHashSet:
    # due to this constraint "At most 10,000 calls will be made to add, remove, and contains" we can use a list wiht at most 10000 elements, time complexity of all the functions will be O(1) and space complexity will be O(10000)

    def __init__(self):
        self.my_hash=list()
        for i in range(1000000+2):
            self.my_hash.append(False)
        

    def add(self, key: int) -> None:
        self.my_hash[key]=True
        

    def remove(self, key: int) -> None:
        self.my_hash[key]=False
        

    def contains(self, key: int) -> bool:
        return self.my_hash[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)