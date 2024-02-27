#preguntar que funcion se desea hacer
#Matemáticas con Python
#FUNCIÓN PARA CALCULO DEL FACTORIAL DE "n"

#def funcion(n):
    



def factoria(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = n * factoria(n - 1)
        return resultado
    
n=int(input("ingrese valor de n : "))

#calculamos el factorial de n
n_factorial = factoria(n)
print (n_factorial)

print("--**--**--**--**--**--**--**--**--**--**--**--**--") 

#definimos una lista vacia
lista=[]
num=int(input("indique cuantos valores desea ingresar: "))

#disponemos un ciclo de n ("num") vueltas
for x in range(num):
    valor=int(input("Ingrese los valores deseados : "))
    lista.append(valor)

#imprimimos la lista    
print(lista)

def multiplicar_elementos_lista(lista):
    multiplicativo= 1

    for numeros in lista:
        multiplicativo *= numeros
    return multiplicativo

print(multiplicar_elementos_lista(lista))

print("fin")

print("--**--**--**--**--**--**--**--**--**--**--**--**--") 