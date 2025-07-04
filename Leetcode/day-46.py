
# 705. Design HashSet
class MyHashSet:

    def __init__(self):
        self.size = 10**6  + 1
        self.data = [False] * self.size

    def add(self, key: int) -> None:
        self.data[key] = True  

    def remove(self, key: int) -> None:
        self.data[key] = False        

    def contains(self, key: int) -> bool:
        return self.data[key]     


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

mySet = MyHashSet()
mySet.add(5)
print(mySet.contains(5))   
mySet.remove(5)
print(mySet.contains(5))   