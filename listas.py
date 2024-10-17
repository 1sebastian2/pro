#crear una lista 
lista = [90,"a","viernas",False,4.5]
print(f"los de la lista son: {lista}")
#datos en lista 
print(lista[2])
print(lista[4])
print(lista[-4])
print(lista[-3])
#recorre un lista 
lista[1:4]
print(lista[1:4])
print(lista[0:3])
print(lista[-1:])
#agregar datos a una lista 
numeros = [1,5]
numeros.append("sebastianortizlara669@gmail.com")
print(numeros)
#tamaño lista 
longitud = numeros.__len__()
print(f"el tamaño de la lista es {longitud}")
#insert
numeros.insert(2,"sebastin")
print(numeros)
#remplazar datos de la lista 
numeros[-1] = "sabastaian@gmail,com"
print(numeros)
numeros[-2] = "sebastian.o"
print(numeros)
#eliminar dato
numeros.remove(1)
print(numeros)
numeros.pop()
print(numeros)
numeros[0:3] =[]
print(numeros)
#recorre lista
for i in lista:
    print(f"dato lista:{i}")
#invertir datos de una lista 
lista.reverse()
print(lista)

#ordenar datos de una lista 
lista_2= [10,2,4,5,7,8,3]

print(sorted(lista_2))
lista_2.sort(reverse=True)
print(lista_2)
print(lista_2[:])







