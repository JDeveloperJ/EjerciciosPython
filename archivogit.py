print("Hola como estas")
print("1.sumar\n2.Restar\n3.multiplicar")
opcion = int(input("Ingresa una opcion a realizar"))
numero1 = int(input("Ingresa el primer numero"))
numero2 = int(input("Ingresa el segundo numero"))

if opcion == 1:
    suma = numero1 + numero2
    print("La suma es:" , suma)
elif opcion == 2:
    if(numero1 < numero2):
        resta = numero2 - numero1
        print("La resta es: " , resta)
    else: 
        resta = numero1 - numero2
        print("La resta es: ", resta)
else:
    mutiplicacion = numero1 * numero2
    print("La multiplicacion es es: " , mutiplicacion)
print("Gracias por haber visitado este programa")



