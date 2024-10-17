#estructura de repeticion 
for i in range(2) : #comienza des cero

    print(f" su dato es {i} ")
for i in range(20,101) : #inicio,fin -1

    print(f" su dato es {i} ") # comienza inicio.fin-1 incremento
for i in range(1,10,2) : 
    print(f" su dato es {i} ")

#estructura de repeticion 
for letra in "python":
    print(letra)

#ejemplo 1
cadena = "python"
for letra in cadena:
    if letra == "y":
        print( "se encontro una y")
        break
    else:
        print("letra no encontrada")
print("esta fuera del ciclo for")

#ejemplo 2
cadena = "progrmacion"
for letra in cadena:
    if letra == "r":
        print( "se encontro la 1 r")
        break
    else:
        print("letra no encontrada")
print("esta fuera del ciclo for")

#ejemplo 2

mul = int(input("Digite la tabla de multiplicar que desea:"))
for i in range (1,12):
    print  (f"2 X {i} = {i*2}")
