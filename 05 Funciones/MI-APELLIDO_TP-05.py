# #Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


for numero in range(0, 101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# ##dígitos que contiene.
numero = int(input("Ingresa un numero"))

numero_absoluto = abs(numero)

cantidad_digitos = len(str(numero_absoluto))

print("El numero tiene", cantidad_digitos ,"Digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma_total = 0

print("Ingresá números enteros para sumarlos. Ingresá 0 para finalizar.")

while True:
    numero = int(input("Ingresá un número: "))
    if numero == 0:
        break
    suma_total += numero

print(f"La suma total de los números ingresados es: {suma_total}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Adivina el número secreto entre 0 y 9!")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intentá de nuevo.")
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("Números pares del 100 al 0 en orden decreciente:")

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

n = int(input("Ingresá un número entero positivo: "))

# Verificar que sea positivo
if n < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(0, n + 1):
        suma += i
    print(f"La suma de los números de 0 a {n} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
# Cantidad de números a ingresar (podés cambiar 100 por otro número para probar)
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresá {cantidad} números enteros:")

for i in range(cantidad):
    numero = int(input(f"Número {i + 1}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
# Cantidad de números a ingresar (podés cambiar 100 por otro número para probar)
cantidad = 100

suma = 0

print(f"Ingresá {cantidad} números enteros:")

for i in range(cantidad):
    numero = int(input(f"Número {i + 1}: "))
    suma += numero

media = suma / cantidad
print(f"\nLa media de los {cantidad} números ingresados es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# Pedir al usuario un número entero
numero = input("Ingresá un número entero: ")

# Invertir los dígitos usando slicing
numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")
