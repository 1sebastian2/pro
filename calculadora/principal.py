#importar libreria arviso diferentes 
from interfas import (menu, opcion_seleccionada, 
                    solicitud_cuadrado, solicitud_circulo,
                    solicitud_triangulo,solicitud_rectangulo,
                    solicitud_pentagono,solicitud_rombo,
                    solicitud_romboide,solicitud_trapecio,
                    mostrar_cuadrado,mostrar_triangulo,
                    mostrar_circulo,mostrar_rectangulo,
                    mostrar_pentagono,mostrar_rombo,
                    mostrar_romboide,mostrar_trapecio)
from figuras import (area_cuadrado,area_triangulo,
                    area_circulo,area_rectangulo,
                    area_pentagono,area_rombo,
                    area_romboide,area_trapecio)

#variables 
opcion = 0
#funcion principal
while opcion != 4:
    op = menu()
    formas_geometricas = opcion_seleccionada(op)
    #condicionales
    if formas_geometricas == 1:
        lado = solicitud_cuadrado()
        area = area_cuadrado(lado)
        mostrar_cuadrado(area)
    elif formas_geometricas == 2:
        base,altura = solicitud_triangulo()
        area = area_triangulo(base,altura)
        mostrar_triangulo(area)
    elif formas_geometricas == 3:
        radio = solicitud_circulo()
        area = area_circulo(radio)
        mostrar_circulo(area)
    elif formas_geometricas == 4:
        base,altura = solicitud_rectangulo()
        area = area_rectangulo(base,altura)
    elif formas_geometricas == 5:
        perimetro,apotema = solicitud_pentagono()
        area = area_pentagono(perimetro,apotema)
        mostrar_pentagono(area)
    elif formas_geometricas == 6:
        base1,base2,altura = solicitud_trapecio()
        area = area_trapecio(base1,base2,altura)
        mostrar_trapecio(area)
    elif formas_geometricas == 7:
        diagonal_mayor,diagonal_menor,altura = solicitud_rombo()
        area = area_rombo(diagonal_mayor,diagonal_menor,altura)
        mostrar_rombo(area)
    elif formas_geometricas == 8:
        base,altura = solicitud_romboide()
        area = area_rombo(base,altura)
        mostrar_romboide(area)
    
    elif formas_geometricas == 9:
        print("saliendo de calculadora ...")
        break
    else:
        print("opcion erronea!!!")
#mensaje
print("gracias por usar la calculadora de figuras!!!")

