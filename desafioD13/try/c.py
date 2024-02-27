def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ingrese valor de n
n = int(input("Ingrese valor de n: "))

# Calculamos el factorial de n
n_factorial = factorial(n)
print(n_factorial)

# Definimos una lista vacía
lista = []
num = int(input("Indique cuántos valores desea ingresar: "))

# Disponemos un ciclo de n ("num") vueltas
for x in range(num):
    valor = int(input("Ingrese los valores deseados: "))
    lista.append(valor)

# Imprimimos la lista    
print(lista)

print("Fin")