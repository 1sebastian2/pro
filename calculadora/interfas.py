#funcion menu principal
def menu ():

    """
    muestra el menu de las figuras geometricas
    retor la variable opcion 
    """
    print("\n bienvenido a la calculadora de figuras ")
    print("1. cuadrado")
    print("2. triangulo")
    print("3. circulo")
    print("4. rectangulo")
    print("5. pentagono")
    print("6. trapecio")
    print("7. rombo")
    print("8. romboide")
    print("9. salir")
    op = int(input("digite una opcion del menu: "))
    return op

#mostrar informamacion seleccionada 

def opcion_seleccionada(op):
    """
    mostrar lo selecciionado del menu
    
    """
    print("\n bienvenido ala calculadora")
    
    #variables
    cuadrado = 1
    triangulo = 2
    circulo = 3
    rectangulo = 4
    pentagono = 5
    trapecio = 6
    rombo = 7
    romboide = 8
    salir = 9
    #condicionales 
    if op == 1:
        print(f"usted selecciono la opcion cuadrado")
        return cuadrado
    elif op == 2:
        print(f"usted selecciono la opcion triangulo")
        return triangulo
    elif op == 3:
        print(f"usted selecciono la opcion circulo")
        return circulo
    elif op == 4:
        print(f"saliendo de la calculadora...")
        return salir
    else:
        print(f"opcion no valida!!!!")
        return "opcion no valida!!!!"

# solicitud de informacion 
# cuadrado
def solicitud_cuadrado ():
    """
    solicita el lado para calculo el 
    area, tipo de dato float
    """
    lado = float(input("digite el lado "))
    return lado

# triangulo
def solicitud_triangulo ():
    """
    solicita base y altura  para calculo el 
    area, tipo de dato float retorna primero la base y despues la altura 
    """
    base = float(input("digite la base "))
    altura = float(input("digite la altura "))
    return base, altura

# circulo
def solicitud_circulo ():
    """
    solicita radio para calculo el 
    area, tipo de dato float
    """
    radio = float(input("digite la radio "))
    return radio

# rectangulo
def solicitud_rectangulo ():
    """
    solicita  para calculo el 
    area, tipo de dato float
    """
    base = float(input("digite la base "))
    altura = float(input("digite la altura "))
    return base, altura
    
#pentagono
def solicitud_pentagono():
    """
    solicita el lado,apotema para calculo el 
    area, tipo de dato float
    """
    lado = float(input("digite la base "))
    apotema = float(input("digite la apotema "))
    return lado, apotema
    
#trapecio
def solicitud_trapecio():
    """
    solicita la base1,base2 y la altura para calculo el 
    area, tipo de dato float
    """
    base1 = float(input("digite la base1 "))
    base2 = float(input("digite la base2 "))
    altura = float(input("digite la altura "))
    return base1,base2, altura
    
#rombo
def solicitud_rombo():
    """
    solicita la diagonal _mayor,diagonal_menor para calculo el 
    area, tipo de dato float
    """
    diagonal_mayor = float(input("digite la diagonal mayor "))
    diagonal_menor = float(input("digite la diagonal menor "))
    return diagonal_mayor,diagonal_menor
    
#romboide
def solicitud_romboide():
    """
    solicita la base, altura para calculo el 
    area, tipo de dato float
    """
    base = float(input("digite la base "))
    altura = float(input("digite la altura "))
    return base,altura
    
#mostrar informacion areas 
#mostrar areas cuadrado
def mostrar_cuadrado(area):
    """
    muestra el area del cuadrado
    tipo float
    """
    print(f"el area del cuadrado es: {area}")

#mostrar areas triangulo
def mostrar_triangulo(area):
    """
    muestra el area del triangulo
    tipo float
    """
    print(f"el area del triangulo es: {area}")
#mostrar areas circulo
def mostrar_circulo(area):
    """
    muestra el area del circulo
    tipo float
    """
    print(f"el area del circulo es: {area}")
#mostrar area del rectangulo
def mostrar_rectangulo(area):
    """
    muestra el area del rectangulo
    tipo float
    """
    print(f"el area del rectangulo es: {area}")
#mostrar area del pentagono
def mostrar_pentagono(area):
    """
    muestra el area del pentagono
    tipo float
    """
    print(f"el area del pentagono es: {area}")
#mostra area del trapecio
def mostrar_trapecio(area):
    """
    muestra el area del trapecio
    tipo float
    """
    print(f"el area del trapecio es: {area}")
#mostrar area del rombo
def mostrar_rombo(area):
    """
    muestra el area del rombo
    tipo float
    """
    print(f"el area del ronbo es: {area}")
#mostrar area del romboide 
def mostrar_romboide(area):
    """
    muestra el area del romboide
    tipo float
    """
    print(f"el area del romboide es: {area}")










