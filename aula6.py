class Deque: #class to create a deque
    def __init__(self):
        self.elements = [] #function to start a list

    def isEmpty(self):
        return self.elements == [] #function to see if the list is empty
    
    def addFront(self, item):
        self.elements.append(item) #function to add an item in the front of the list

    def addRear(self, item):
        self.elements.insert(0, item) #function to add an item in the rear(back) of the list

    def removeFront(self):
        return self.elements.pop() #function to remove the last item was added in the list
    
    def removeRear(self):
        return self.elements.pop(0) #function to remove the item that is in in the front of the list
    
    def size(self):
        return len(self.elements) #functiom to verify the size of the list
    

from aula6 import Deque

deque = Deque()

print(deque.isEmpty)
deque.addRear(10)
deque.addRear(20)
deque.addFront('Ab')
deque.addFront(True)
print(deque.size())
print(deque.isEmpty())
deque.addRear(5.5)
print(deque.removeRear())
print(deque.removeFront())
print(deque)