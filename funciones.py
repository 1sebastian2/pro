#funcion 
def  mensaje():
    """
    mostrar mensaje programacion 1: str
    
    """
    print("programacion 1")
    x=10
#llamar funcion 
mensaje()
print()
#crear funcion con parametros 
def suma (num1,num2):
    """
    generar la suma de dos numeros 
    enteros con variables de entrada 
    num1,num2
    """
    rta = num1 + num2
    print(f"la suam entre {num1} + {num2} = {rta}")

# llamar funcion 
suma(1,2)

#funcion pedir datos 
def solicitar_datos():
    """
    solicita num1 y num2, tranforma a tipo de dato 
    entero y retorna la informacion 
    """
    num1 = int(input("digite el numero 1: "))
    num2 = int(input("digite el numero 2: "))
    return num1,num2

#llamar funcion 
a,b = solicitar_datos()
print(f"nuemros digitados {a} y {b}")
#llamar a suma 
suma(a,b)

#funcion multiplicacion 
def multiplicacion (num1,num2):
    """
    2 numeros de tipo entero y los retorna 
    
    """
    rta = num1 * num2
    return rta

rta = multiplicacion(a,b)
print(f"el resultado de la * = {rta}")

suma (rta,a)