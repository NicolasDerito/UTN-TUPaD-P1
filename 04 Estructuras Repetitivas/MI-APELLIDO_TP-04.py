#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):  
    print(numero)

 #2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.   

numero = int(input("Ingrese un numero: "))
numero_abs = abs(numero)
cantidad_digitos= len(str(numero_abs))
print("El numero tiene", cantidad_digitos, "digito(s).")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
# Pedimos los dos valores al usuario
inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número: "))


if inicio > fin:
    inicio, fin = fin, inicio 

suma = 0 


for numero in range(inicio + 1, fin):
    suma += numero

print("La suma de los números entre", inicio, "y", fin, "es:", suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
inicio = int(input("Ingresa el primer numero: "))
fin = int(input("Ingresa el segundo numero: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for numero in range(inicio + 1, fin):
    suma += numero

print("La suma de los numeros entre", inicio, "y", fin, "es:", suma )

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_secreto = random.randint(0,9)
intentos = 0

while True:
    intento = int(input("Adivina el numero (entre 0 y 9)"))
    intentos +=  1

    if intentos == numero_secreto:
        print("¡Correcto! Adivinaste el numero.")
        break
    else:
        print("No, intenta de nuevo.")

print("Cantidad de intentos: ", intentos)