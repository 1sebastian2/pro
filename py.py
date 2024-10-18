#Tablero de ajedrez
# Solicitar el tamaño del tablero al usuario
filas = int(input("Introduce el número de filas del tablero: "))
columnas = int(input("Introduce el número de columnas del tablero: "))

# Crear el tablero de ajedrez
tablero_ajedrez = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        if (i + j) % 2 == 0:
            fila.append('■')
        else:
            fila.append("□")
    tablero_ajedrez.append(fila)

# Imprimir el tablero de ajedrez
for fila in tablero_ajedrez:
    for casilla in fila:
        print(casilla, end=" ")
    print()  # Nueva línea al final de cada fila