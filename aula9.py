def bublleSort(list):
    for passnum in range(len(list)-1, 0, -1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux


lista = [20, 5, 22, 3, 30, 27]
bublleSort(lista)
print(lista)