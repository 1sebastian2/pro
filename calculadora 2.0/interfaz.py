def menu():
    """
    Muestra el menú de las figuras geométricas y retorna la opción seleccionada.
    """
    opciones = [
        "1. Cuadrado", "2. Triángulo", "3. Círculo", "4. Rectángulo",
        "5. Pentágono", "6. Trapecio", "7. Rombo", "8. Romboide", "9. Salir"
    ]
    print("\nBienvenido a la calculadora de figuras")
    print("\n".join(opciones))
    return int(input("Seleccione una opción del menú: "))

def mostrar_area(figura, area):
    """
    Muestra el área calculada de la figura.
    """
    print(f"El área del {figura} es: {area}")

def solicitar_valores(*nombres):
    """
    Solicita los valores necesarios para calcular el área.
    """
    return [float(input(f"Ingrese {nombre}: ")) for nombre in nombres]