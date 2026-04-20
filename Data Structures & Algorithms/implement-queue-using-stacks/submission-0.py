class MyQueue:

    def __init__(self):
        self.myqueue1 = []
        self.myqueue2 = []

    def push(self, x: int) -> None:
        self.myqueue1.append(x)

    def pop(self) -> int:
        if not self.myqueue2:
            while self.myqueue1:
                self.myqueue2.append(self.myqueue1.pop())
        return self.myqueue2.pop()

    def peek(self) -> int:
        if not self.myqueue2:
            while self.myqueue1:
                self.myqueue2.append(self.myqueue1.pop())
        return self.myqueue2[-1]

    def empty(self) -> bool:
        return len(self.myqueue1) == 0 == len(self.myqueue2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()