def mostrar_menu():
    print("Seleccione una opción:")
    print("1. PlayStation - $1,000,000")
    print("2. Xbox - $5,000,000")
    print("3. Salir")

def obtener_precio(opcion):
    if opcion == 1:
        return 1000000
    elif opcion == 2:
        return 5000000
    else:
        return 0

nombre = input("Ingrese su nombre: ")
print(f"Bienvenido, {nombre}!")

productos_comprados = []

while True:
    mostrar_menu()
    entrada = input("Ingrese el número de su opción: ")
    
    if entrada.isdigit():
        opcion = int(entrada)
        if opcion == 3:
            print("Gracias por su visita.")
            break
        
        precio = obtener_precio(opcion)
        if precio > 0:
            productos_comprados.append((opcion, precio))
            continuar = input("¿Desea comprar otro producto? (si/no): ")
            if continuar == 'no':
                break
        else:
            print("Opción no válida. Intente de nuevo.")
    else:
        print("Por favor, ingrese un número válido.")

total = sum(precio for _, precio in productos_comprados)
for opcion, precio in productos_comprados:
    if opcion == 1:
        producto = "PlayStation"
    elif opcion == 2:
        producto = "Xbox"
    print(f"Compraste: {producto}, Precio: ${precio}")

print(f"Total de compras: ${total}")
print("Compra exitosa.")