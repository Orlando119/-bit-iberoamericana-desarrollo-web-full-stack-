numero = int(input("Ingresa un numero  " ))
solucion=i
while numero<0:
    print(" has introducido un numero negativo, vuelve a intentarlo")
    numero= int(input("Ingresa un numero " ))
    i=math.sqrt(numero)
print("La raiz cuadrada del numero " + str (numero) + "es"
+ str (i))
