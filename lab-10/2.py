class Stack:
    def __init__(self, k):
        self.k = k
        self.stack = []
    
    def push(self, item):
        if len(self.stack) < self.k:
            self.stack.append(item)
        else:
            pass
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None 

stack = Stack(k=5)
for i in range(10):  
    stack.push(i)
    if i % 2 == 0:
        print(f"Popped: {stack.pop()}")
