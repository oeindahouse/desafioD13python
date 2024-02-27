n=int(input("ingrese valor de n: "))
def factoria(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = n * factoria(n - 1)
        return resultado

#calculamos el factorial de n
n_factorial = factoria(n)
print (n_factorial)