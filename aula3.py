class Node:
    def __init__(self, element):
        self.data = element
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
       self.data = newdata

    def setNext(self,newnext):
       self.next = newnext

class orderedList:
    def __init__(self):
       self.head = None
    def search(self,element):
       current = self.head
       found = False
       stop = False
       while current != None and not found and not stop:
           if current.getData() == element:
               found = True
           else:
               if current.getData() > element:
                   stop = True
               else:
                   current = current.getNext()
       return found
    def add(self,element):
       current = self.head
       previous = None
       stop = False
       while current != None and not stop:
           if current.getData() > element:
               stop = True
           else:
               previous = current
               current = current.getNext()
       temp = Node(element)
       if previous == None:
           temp.setNext(self.head)
           self.head = temp
       else:
           temp.setNext(current)
           previous.setNext(temp)
    def isEmpty(self):
       return self.head == None
    def size(self):
       current = self.head
       count = 0
       while current != None:
           count = count + 1
           current = current.getNext()
       return count
