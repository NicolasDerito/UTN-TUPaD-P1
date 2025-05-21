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

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for numero in range(100 , -1, -1):
    if numero % 2 == 0:
        print (numero)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

limite = int(input("Ingresa un numero entero positivo: "))

suma = 0

for numero in range(0, limite + 1):
    suma += numero

    print("La suma de los numeros desde 0 hasta", limite, "es", suma)



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingresa el numero {i + 1}:"))

    if numero % 2 == 0:
        pares += 1 
    
    else:
        impares += 1

    
    if numero > 0:
        positivo += 1
    elif numero< 0:
        negativos += 1

    print ("\nRESULTADOS:")
    print ("Cantidad de numeros pares:", pares)
    print ("Cantidad de numeros impares:", impares)
    print ("Cantidad de numeros positivos: ", positivo)
    print ("Cantidad de numeros positivos:", negativos)

   # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 100


suma = 0


for i in range(cantidad):
    numero = int(input(f"Ingrésa el número {i + 1}: "))
    suma += numero


media = suma / cantidad

print("\nLa media de los", cantidad, "números ingresados es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = input("Ingresá un número: ")

numero_invertido = numero[::-1]

print("El número invertido es:", numero_invertido)

print("cant")