# Desarrollar un algoritmo que calcule el promedio de un arreglo de
# reales.

# Ejemplos de arreglos
import math as mt
Lista_1 = [1,2,3] # Ejemplo de lista vacia
Lista_2 = [1, -2, 3.5, mt.pi] # Ejemplo de lista con números reales y un valor irracional importado desde la libreria "math"

def calcular_promedio (lista_a_promediar): 
    
    # Aqui se verifica si la lista suministrada 
    # se encuentra vacía
    if len(lista_a_promediar) == 0:
        return print ("Su lista esta vacia")
    else:
        # En caso de que la lista no este vacía se realiza
        # el cálculo del promedio de los indices de la lista
        suma_reales = 0

        for numero_real in lista_a_promediar:
            suma_reales += numero_real

        cantidad_de_numeros = len (lista_a_promediar) # Se calcula la cantidad de elementos de la lista
        resultado = suma_reales / cantidad_de_numeros # Calculo del promedio de los 
        
        return print (f"El promedio de su arreglo es de: {resultado}")

# Aplicación de la funcion calcular promedio para ambas listas
calcular_promedio (Lista_1)
calcular_promedio (Lista_2)