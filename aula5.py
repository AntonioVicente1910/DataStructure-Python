#Classe para se criar uma fila

class Queue:
#criar as funções para gerir e controlar a fila
    def __init__(self):
        self.elements = []
        #função que gera uma fila vazia
    def enqueue(self, item):
        self.elements.insert(0, item)
        #função para inserir elemento na fila
    def isEmpty(self):
        #return self.elements == []
        if len(self.elements) == 0:
            print('Fila vazia')
        else:
            print('Lista preenchida')
        #verifica se a fila eta vazia
    def size(self):
        #return len(self.elements)
        tam = len(self.elements)
        return print (f'A lista possui {tam} elementos!')
    def dequeue(self):
       return self.elements.pop()
        #verifica o tamanho da fila e retorna o tamanho

fila = Queue()
print(fila.size())
print(fila.isEmpty())
fila.enqueue(10)
fila.enqueue(20)
print(fila.size())
print(fila.isEmpty())
print(fila)
fila.enqueue("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(fila)
fila.dequeue
print(fila.size())
print(fila)