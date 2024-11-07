# Función del menú principal
def menu():
    """
    Muestra el menú de las figuras geométricas
    Retorna la variable opción 
    """
    print("\nBienvenido a la calculadora de áreas")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Círculo")
    print("4. Pentágono")
    print("5. Trapecio")
    print("6. Rombo")
    print("7. Romboide")
    print("8. Rectángulo")
    print("9. Salir")
    op = int(input("Digite una opción del menú: "))
    return op

# Mostrar información de la opción seleccionada
def opcion_seleccionada(op):
    """
    Muestra la opción seleccionada del menú
    """
    print("\nBienvenido a la calculadora de áreas")
    
    # Opciones
    opciones = {
        1: "Cuadrado",
        2: "Triángulo",
        3: "Círculo",
        4: "Pentágono",
        5: "Trapecio",
        6: "Rombo",
        7: "Romboide",
        8: "Rectángulo",
        9: "Salir"
    }
    if op in opciones:
        print(f"Usted seleccionó la opción {opciones[op]}")
        return op
    else:
        print("¡Opción no válida!")
        return None

# Funciones para solicitar datos
def solicitud_cuadrado():
    lado = float(input("Digite el lado: "))
    return lado

def solicitud_triangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base, altura

def solicitud_circulo():
    radio = float(input("Digite el radio: "))
    return radio

def solicitud_pentagono():
    lado = float(input("Digite el lado del pentágono: "))
    apotema = float(input("Digite la apotema del pentágono: "))
    return lado, apotema

def solicitud_trapecio():
    base_mayor = float(input("Digite la base mayor: "))
    base_menor = float(input("Digite la base menor: "))
    altura = float(input("Digite la altura: "))
    return base_mayor, base_menor, altura

def solicitud_rombo():
    diagonal_mayor = float(input("Digite la diagonal mayor: "))
    diagonal_menor = float(input("Digite la diagonal menor: "))
    return diagonal_mayor, diagonal_menor

def solicitud_romboide():
    base = float(input("Digite la base del romboide: "))
    altura = float(input("Digite la altura del romboide: "))
    return base, altura

def solicitud_rectangulo():
    base = float(input("Digite la base del rectángulo: "))
    altura = float(input("Digite la altura del rectángulo: "))
    return base, altura

# Funciones para mostrar áreas
def mostrar_area(figura, area):
    """
    Muestra el área de la figura
    """
    print(f"El área del {figura} es: {area}")

# Funciones para calcular áreas
def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    import math
    return math.pi * (radio ** 2)

def calcular_area_pentagono(lado, apotema):
    perimetro = 5 * lado
    return (perimetro * apotema) / 2

def calcular_area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_romboide(base, altura):
    return base * altura

def calcular_area_rectangulo(base, altura):
    return base * altura

# Programa principal
while True:
    opcion = menu()
    if opcion == 1:
        lado = solicitud_cuadrado()
        area = calcular_area_cuadrado(lado)
        mostrar_area("cuadrado", area)
    elif opcion == 2:
        base, altura = solicitud_triangulo()
        area = calcular_area_triangulo(base, altura)
        mostrar_area("triángulo", area)
    elif opcion == 3:
        radio = solicitud_circulo()
        area = calcular_area_circulo(radio)
        mostrar_area("círculo", area)
    elif opcion == 4:
        lado, apotema = solicitud_pentagono()
        area = calcular_area_pentagono(lado, apotema)
        mostrar_area("pentágono", area)
    elif opcion == 5:
        base_mayor, base_menor, altura = solicitud_trapecio()
        area = calcular_area_trapecio(base_mayor, base_menor, altura)
        mostrar_area("trapecio", area)
    elif opcion == 6:
        diagonal_mayor, diagonal_menor = solicitud_rombo()
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        mostrar_area("rombo", area)
    elif opcion == 7:
        base, altura = solicitud_romboide()
        area = calcular_area_romboide(base, altura)
        mostrar_area("romboide", area)
    elif opcion == 8:
        base, altura = solicitud_rectangulo()
        area = calcular_area_rectangulo(base, altura)
        mostrar_area("rectángulo", area)
    elif opcion == 9:
        print("Saliendo de la calculadora...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
