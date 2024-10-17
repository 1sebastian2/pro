#declarar una matriz 
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 =[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#recorrer una matriz 
for filas in matriz1:
    for elementos in filas :
        print(f"elementos matriz: {elementos}, {filas}")
matriz3 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    
]
for filas in matriz3:
    for elementos in filas :
        print(f"elementos matriz: {elementos}, {filas}")

#tamaño matriz
f=len(matriz3)
print(f"tamaño filas: {f}")
c = len(matriz3 [2])
print(f"tamaño columnas: {c}")

#receorrer matriz con range
for i in range(f):
    for j in range(c):
        print(f"posicion {i},{j}: {matriz1 [i][j]}")
print(matriz1[1][2])


