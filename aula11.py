sala10 = ["Alice", "Bruno", "Carlos", "Diana"]
sala11 = ["Eduarda", "Carlos", "Fernanda", "Gabriel"]
sala12 = ["Helena", "Carlos", "Isabela", "João"]

def sequentialSearch(list, element):
    pos = 0
    found = False

    while pos < len(list) and not found:
        if list[pos] == element:
            found = True
        
        else:
            pos = pos+1
    return found

print(sequentialSearch(sala10, 'Carlos'))

print(sequentialSearch(sala11, 'Carlos'))

print(sequentialSearch(sala12, 'Gabriel'))