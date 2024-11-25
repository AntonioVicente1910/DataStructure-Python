#from aula11 import sala10, sala11, sala12

def binarySearch(list, element):
    first = 0
    last = len(list)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == element:
            found = True
        else:
            if element < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def recursiveBinarySearch(list, element):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == element:
            return True
        else:
            if element<list[midpoint]:
                return binarySearch(list[:midpoint], element)
            else:
                return binarySearch(list[:midpoint+1:], element)


sala10 = ["Alice", "Bruno", "Carlos", "Diana"]
sala11 = ["Eduarda", "Carlos", "Fernanda", "Gabriel"]
sala12 = ["Helena", "Carlos", "Isabela", "João"]

print(recursiveBinarySearch(sala10, "Carlos"))
print(recursiveBinarySearch(sala11, "Rogéria"))

print(sala10)