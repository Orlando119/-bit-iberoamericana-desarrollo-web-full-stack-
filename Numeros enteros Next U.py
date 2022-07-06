##escribir un programa que dado un número entero muestre su valor absoluto 
#nota para los dos números positivos su valor absoluto es igual al número mientras que para los negativos su valor absoluto es el número multiplicado por menos 1 
numero = float (input ( "Ingrese un numero"))
if numero  > 0 :
    print (" El valor absoluto de  " + str (numero) +" "+"es posivo")
elif numero <0 :
     numero = numero*-1
     print ("El valor absoluto es ",numero
     )
