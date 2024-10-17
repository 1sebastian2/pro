# variables 
opcion = 0
#estructura repeticion 

while opcion != 7:

    #menu calculadora
    print("\nhola calculadora")
    print("1. suma")
    print("2. resta")
    print("3. multiplicasion")
    print("4. division")
    print("5. potencia")
    print("6. divicon por cero ")
    print("7. salir")
    
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
        elif opcion == 6:
            num  = int(input("digite el primer numero: "))
        if  num <0:
            print("error no se puede calcular")
            
        elif opcion == 7:
            print(f"saliendo de la calculadora...")
        else:
            print("error")
    except ValueError:
        print("ingrese una opcion valida")
print("gracias por utilizar la calculadora")








































































































































#git init = Crea un reposotorio local
#git add "nombre de archivo" = Guarda el archivo en el repositorio local, entra en la fase modificación.
#git commit -m "comentario" = Confirma los cambios
#git remote add origin "dirección del repositorio remoto".
#git branch -M "Rama que se está utilizando".
#git push -u origin "Rama que se está utilizando".
#git config --global user.name "Tu Nombre"
#git config --global user.email "tu_email@example.com"


#Es un lenguaje interpretado, no compilado.
#Usa tipado dinámico, lo que significa que una variable puede tomar valores de distinto tipo.
#Es fuertemente tipado, lo que significa que el tipo no cambia de manera repentina. Para que se produzca un cambio de tipo tiene que hacer una conversión explícita.
#Es multiplataforma, ya que un código escrito en macOS funciona en Windows o Linux y vice versa.