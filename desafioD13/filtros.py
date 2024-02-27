#para ingresar argumentos por cmd con pyhton cifra > o <
import sys

#definir funcion con diccionario precios, umbral y funcion mayor que se pide
def filtrar_productos_umbral(precios, umbral, operacion):
    #comprobacion de funcion
    if operacion == 'mayor':
        precios_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
    elif operacion == 'menor':
        precios_filtrados = [producto for producto, precio in precios.items() if precio < umbral]
    else:
        return "Lo sentimos, no es una operación válida"

    return precios_filtrados

if __name__ == "__main__":
    #diccionario de precios  productos
    precios = {
            'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000
            }

    #obtener valores de la linea de comandos
    args = sys.argv[1:]
#while operacion=
    if len(args) == 2:
        umbral = int(args[0])
        operacion = args[1].lower()
        productos_filtrados = filtrar_productos_umbral(precios, umbral, operacion)
    else:
        print("Lo sentimos, no es una operación válida")
        sys.exit(0)

    #imprimir resultados
    if isinstance(productos_filtrados, list):
        if productos_filtrados:
            print(f"Los productos {operacion}al umbral son: {', '.join(productos_filtrados)}")
        else:
            pass
    else:
        print(productos_filtrados)
