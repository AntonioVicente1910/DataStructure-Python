class Stack:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
       return self.elements == []
    def push(self, item):
        self.elements.append(item)
    def pop(self):
        return self.elements.pop()
    def peek(self):
        return self.elements[len(self.elements) - 1]
    def size(self):
        return len(self.elements)
    
pilha = Stack()
print (pilha.isEmpty())
pilha.push(20)
pilha.push(30)
pilha.push(pilha.peek())
pilha.push(True)
print(pilha.size())
print(pilha.isEmpty())
pilha.push('AB')
print(pilha.pop())
print(pilha.pop())
print(pilha.size())


