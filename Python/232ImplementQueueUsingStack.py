class MyQueue:

    def __init__(self):
        self.inStack, self.outStack = [], []
        self.front = None 

    def push(self, x: int) -> None:
        if not self.inStack:
            self.front = x 
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        ans = self.outStack.pop()
        return ans

    def peek(self) -> int:
        if self.outStack:
            return self.outStack[-1]
        return self.front
        

    def empty(self) -> bool:
        return (not self.inStack) and (not self.outStack)
    
    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()