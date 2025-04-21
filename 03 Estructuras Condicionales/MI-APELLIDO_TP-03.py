# 1)

#Se ingresa un input para que el usuario coloque su edad
edad = int(input ("Ingrese su edad por favor: "))
# se realiza un if para poner en rango si es mayor o menor
if edad >= 18:
        print("Es mayor")
else:
        print("Es menor de edad")



# 2)

nota = int(input("ingrese su nota por favor: "))

if nota >= 6:
        print ("Aprobado")
else:
        print ("Desaprobado")


# 3) 

par = int(input("Por favor ingrese un numero: "))

if par % 2 == 0:
        print ("Ha ingresado un numero par")
else:
        print ("Ha ingresado un numero inpar")

#4)

#Se define la variable edad para hacer un input y que el usuario ingrese su edad
edad = int(input("Por favor ingrese su edad: "))
#aca se utiliza varias condiciones y rangos segun corresponda
if edad < 12:
        print ("menor de 12 años")
elif edad >= 12 and edad < 18:
        print ("Adolecente: mayor o igual que 12 y menor que 18 años")
elif edad >= 18 and edad < 30:
        print ("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
        print("Adulto/a: mayor o igual que 30 años.")

# 5)
# Pedir al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificar la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6 )
import random
from statistics import mean, median, mode

# Lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]

# Calcular medidas estadísticas
media = mean(numeros)
mediana = median(numeros)
moda = mode(numeros)  

# Mostrar resultados
print("Lista generada:", numeros)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Detectar tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print(" No hay un sesgo claro")


# 7 )
# Solicita una frase o palabra al usuario
texto = input("Ingresá una frase o palabra: ")

# Verifica si termina con una vocal (mayúscula o minúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"  # Agrega el signo de exclamación

# Imprime el resultado
print("Resultado:", texto)

# 8)
#Pedir nombre al usuario
nombre = input("Ingrese su nombre: ")

# Mostrar opciones

print("¿Como queres ver tu nombre?")
print("1. Todo MAYUSCULAS")
print("2. Todo en minusculas")
print("3. Solo la primera letra en mayusculas")

#Pedir opcion al usuario

opcion = input ("elegi 1, 2 o 3: ")

#Transformar el nombre segun la opcion elegida

if opcion == "1":
       print("Resultado: ", nombre.upper())
elif opcion == "2":
       print("Resultado: ", nombre.lower())
elif opcion == "3":
        print("Resultado:", nombre.title())
else:
       print("Opcion no valida")

#9)
terremoto = int(input("Por favor ingrese la magnitud del terremoto: "))

if terremoto < 3:
       print("Muy leve, imperceptible ")
elif terremoto >= 3 and terremoto < 4:
       print ("Leve, ligeramente perceptible")
elif terremoto >= 4 and terremoto < 5:
       print ("Moderado, sentido por personas, pero generalmente no causa daños")

elif terremoto >= 5 and terremoto < 6:
       print ("Fuerte, puede causar daños en estructuras débiles")
elif terremoto >= 6 and terremoto < 7:
       print ("Muy fuerte,puede causar daños significativos ")
else :
       print ("Extremo, puede causar graves daños a gran escala")

# 10 )

hemisferio = input ("Ingresa en que hemisfero te encuentras (N/S): ").upper
mes = int(input ("¿En que mes estamos? (1-12): "))
dia = int(input ("¿Que dia es?"))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
       estacion_norte ="Invierno"
       estacion_sur = "Verano"
elif (mes == e and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
       estacion_norte = "primavera"
       estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8 ]) or (mes == 9 and dia <= 20):
       estacion_norte = "Verano"
       estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
       estacion_norte = "Otoño"
       estacion_sur = "Primavera"
else:
       print("Fecha invalida.")
       exit()
       
if hemisferio == "N":
       print  ("Estas en", estacion_norte)
elif hemisferio == "S":
       print("Estas en", estacion_sur)
else:
       print("Hemisferio invalido.")
