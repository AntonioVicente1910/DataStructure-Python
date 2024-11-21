numeros = [184, 29, 23, 33, 140, 77, 80, 76, 141, 49, 104, 126, 136, 128, 6, 146, 36, 43, 181, 196, 163, 142, 59, 116, 56, 42, 15, 56, 151, 158, 66, 184, 58, 92, 113, 14, 24, 33, 19, 153, 81, 6, 181, 62, 82, 85, 9, 65, 59, 90]


# Método com o selectionSort
def selectionSort(list):
    for fillslot in range(len(list)-1, 0, -1):
        positionOfMax = 0
        for location in range (1, fillslot + 1):
            if list[location]>list[positionOfMax]:
                positionOfMax = location
        
        aux = list[fillslot]
        list[fillslot] = list[positionOfMax]
        list[positionOfMax] = aux

# selectionSort(numeros)

# Método com o insertionSort

def insertionSort(list):
    for index in range(1, len(list)):

        currentValue = list[index]
        position = index

        while position>0 and list[position-1]>currentValue:
            list[position] = list[position-1]
            position = position-1
        
        list[position] = currentValue
    
insertionSort(numeros)
print(numeros)