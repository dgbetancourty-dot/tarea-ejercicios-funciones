# Funcion que calcula el promedio
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 +  nota2 + nota3) / 3
    return promedio 


# Entrada de Datos 
nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))


# Llamada a la funcion 
resultado = calcular_promedio(nota1, nota2, nota3)


# mostrar resultado

print("El promedio es:", resultado)