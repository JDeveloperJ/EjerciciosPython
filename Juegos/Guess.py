import random
minNum = 1 
maxNum = 20
comprobar = True

numero = random.randint(minNum,maxNum)

print("Hola,Bienvenido al Juego, ¡Adivina el numero!")
nombre = input(print("¿Cual es tu nombre?"))
print("Bien " + str(nombre) + " Adivina el numero que esta entre los numeros " + str(minNum) + " y " + str(maxNum))

while comprobar == True:
    numero_ingresado = int(input("Adivina el numero"))
    if numero_ingresado < numero :
        print("El numero ingresado es muy bajo")
    elif numero_ingresado > numero:
        print("El numero ingresado es muy elevado")
    else:
        print("!Bien hecho! " + str(nombre)+ " has adivinado el numero")
        break