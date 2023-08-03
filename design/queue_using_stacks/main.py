class MyQueue:

    def __init__(self):
        self.inner = []
        self.outer = []

    def push(self, x: int) -> None:
        self.inner.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outer.pop()


    def peek(self) -> int:
        if not self.outer:
            while self.inner:
                self.outer.append(self.inner[-1])
                self.inner.pop()
        return self.outer[-1]

    def empty(self) -> bool:
        return len(self.inner) + len(self.outer) == 0