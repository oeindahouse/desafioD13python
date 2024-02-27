



#definimos una lista vacia
lista=[]
num=int(input("indique cuantos valores desea ingresar: "))

#disponemos un ciclo de n ("num") vueltas
for x in range(num):
    valor=int(input("Ingrese los valores deseados : "))
    lista.append(valor)

#imprimimos la lista    
print(lista)

#def multiplicar_elementos_lista(lista):
multiplicativo= 1

for numeros in lista:
    multiplicativo *= numeros

return multiplicativo



#print(multiplicar_elementos_lista(lista))
