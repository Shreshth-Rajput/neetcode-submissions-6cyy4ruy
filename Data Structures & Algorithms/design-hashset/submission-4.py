class LinkedNode:
    def __init__(self, key):
        self.next = None
        self.key = key


class MyHashSet:

    def __init__(self):
        self.hashmap = [LinkedNode(0) for i in range(10**4)]


    def add(self, key: int) -> None:
        cur = self.hashmap[key % len(self.hashmap)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = LinkedNode(key)
         

    def remove(self, key: int) -> None:
        cur = self.hashmap[key % len(self.hashmap)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
        cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hashmap[key % len(self.hashmap)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)