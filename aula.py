def matriz(nLinhas, nColunas, valor):
    matriz = []
    for i in range(nLinhas):
        linha = []
        for j in range(nColunas):
            linha += [valor]
        matriz += [linha]

    return matriz


def imprimeMatriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            print( str(matriz[i][j]) + " | ", end="")
        print("\n")

a = matriz(6, 6, 0)
imprimeMatriz(a)

matriz[2][5] = 1

imprimeMatriz(a)