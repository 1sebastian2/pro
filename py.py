
tablero = [['' for _ in range(8)] for _ in range(8)]


for fila in range(6):
    for columna in range(6):
        if (fila + columna) % 2 == 0:
            tablero[fila][columna] = '■'  
        else:
            tablero[fila][columna] = '□'  


for fila in tablero:
    print(' '.join(fila))