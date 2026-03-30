class LinkedNode:
    def __init__(self, key = -1, value = -1, next = None):
        self.value = value
        self.key = key
        self.next = next


class MyHashMap:

    def __init__(self):
        self.map = [LinkedNode() for i in range(1000)]


    def put(self, key: int, value: int) -> None:
        idx = key % len(self.map)
        cur = self.map[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = LinkedNode(key, value)




    def get(self, key: int) -> int:
        idx = key % len(self.map)
        cur = self.map[idx]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

        

    def remove(self, key: int) -> None:
        idx = key % len(self.map)
        cur = self.map[idx]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)