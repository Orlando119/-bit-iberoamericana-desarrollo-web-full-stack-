numero1 = int (input (" Introduce el primer numero " ))
numero2 = int (input (" Introduce el segundo numero " ))
if numero1%numero2==0:
   print ("el numero " + "" +str (numero1) + "es multiplo  de " + str(numero2))
else:
       print("el numero " + str (numero1) + " NO es multiplo  de " + str(numero2))
if numero2%numero1==0:
    print ("el numero " + " "+ str (numero2) + "es multiplo  de " + str (numero1))
else:
       print("el numero " + str (numero2) + " NO es multiplo  de " + str(numero1))
