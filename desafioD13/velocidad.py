
#lista velocidad entregada por el ej
velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#definir acumulador y contador para suma y promedio 
suma=0
largo_elementos= len(velocidad)

#for para recorrer los elementos de la lista que serán sumados
for velo in velocidad:
    suma=suma + velo
#impresion por consola de la suma
print(f"la suma es: {suma}")

#calculo de promedio e impresion por consola de promedio
promedio = suma / largo_elementos
print(f"el promedio es: {promedio}")

#nueva lista vacia que se llenara con las velocidades mayores en promedio
velocidades_filtradas = []
#for para comprobacion de velocidades que entraran en la lista vacia anterior
for velo in velocidad:
    if velo > promedio:
        velocidades_filtradas.append(velo)

velocidades_filtradas.sort()

print(velocidades_filtradas)





