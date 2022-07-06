
nomCripto= input ("Ingrese el nombre de la criptomoneda : ")
valorDia =float( input("Ingrese el valor en dolares para hoy de cotizacion de la criptomoneda  : " + str (nomCripto)))
cantDias =  float ( input ( " Ingrese la cantidad de diaz tranzados de la criptomoneda " + str (nomCripto)))
porcentGanancia = cantDias*5/100
ganaciaTotal = valorDia *cantDias + porcentGanancia
import datetime
ahora=datetime.datetime.now()
print ("La ganacia total  de inversion en la crptomoneda " + " " + str (nomCripto) + "en " + (cantDias) + " dias tranzados es de " + str (ganaciaTotal) )
print (" esta informacion se imprime en la fecha y hora " + str (ahora))
