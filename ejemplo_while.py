# variables 
opcion = 0
#estructura repeticion 

while opcion != 6:

    #menu calculadora
    print("\nhola calculadora")
    print("1. suma")
    print("2. resta")
    print("3. multiplicasion")
    print("4. division")
    print("5. potencia")
    print("6. salir")
    
    #opcion a ingresar
    try:
        opcion = int(input("digite la opcion de la calculadora "))
        if opcion == 1:
            num1 = int(input("digite el primer numero: "))
            num2 = int(input("digite el segundo numero: "))
            resultado = num1 + num2
            print(f"suma = {resultado}")
        elif opcion == 2:
            num1 = int(input("digite el primer numero: "))
            num2 = int(input("digite el segundo numero: "))
            resultado = num1 - num2
            print(f" resta = {resultado}")
        elif opcion == 3:
            num1 = int(input("digite el primer numero: "))
            num2 = int(input("digite el segundo numero: "))
            resultado = num1 * num2
            print(f"multiplicasion = {resultado}")
        elif opcion == 4:
            num1 = int(input("digite el primer numero: "))
            num2 = int(input("digite el segundo numero: "))
            resultado = num1 / num2
            print(f" divicion = {resultado}")
        elif opcion == 5:
            base = int(input("digite el primer numero: "))
            potencia = int(input("digite el segundo numero: "))
            resultado = base ** potencia
            print(f" potencia = {resultado}")
print("gracias por utilizar la calculadora")




