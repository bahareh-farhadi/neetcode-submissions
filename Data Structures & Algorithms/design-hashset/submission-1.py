class MyHashSet:

    def __init__(self):
        self.my_hash=list()
        

    def add(self, key: int) -> None:
        if len(self.my_hash)==0:
            self.my_hash.append(key)
        else:
            for i in range(len(self.my_hash)):
                if self.my_hash[i]==key:
                    return
            self.my_hash.append(key)
        
        

    def remove(self, key: int) -> None:
        index=-1
        for i in range(len(self.my_hash)):
            if self.my_hash[i]==key:
                index=i
                break
        if index!=-1:
            del self.my_hash[index]
        

    def contains(self, key: int) -> bool:
        for num in self.my_hash:
            if num==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)