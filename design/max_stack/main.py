class MaxStack_list:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = []
        self.max_val = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.head.append(x)
        self.max_val = max(self.max_val, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.head.pop()
        self.max_val = max(self.head)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.head[-1] if self.head else None

    def peekMax(self):
        """
        Retrieve the maximum element in the stack.
        :rtype: int
        """
        return self.max_val

    def popMax(self):
        """
        Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
        :rtype: void
        """
        v = self.max_val
        self.head.remove(self.max_val)
        self.max_val = max(self.head)
        return v