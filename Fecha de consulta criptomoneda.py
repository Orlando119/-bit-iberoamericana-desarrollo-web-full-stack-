nombCripto = input ("Ingrese el nombre de la criptomoneda : ")
CantCripto = float(input("Ingrese la cantidad de criptomoneda " + str (nombCripto)))
cantDias = int(input("Ingrese la cantidad de dias tranzados de la criptomoneda " + str(nombCripto)))
porcentGanacia= float(input("Ingrese el porcentage de ganacia por dia de la criptomoneda " + str(nombCripto)))

totalGanancia = CantCripto*porcentGanacia/100*cantDias
total=CantCripto+totalGanancia
print (" su criptompneda " + str ( nombCripto)+ " ha tenido un pórcentage de ganacia de " + str (porcentGanacia)+ " por ciento en " +str (cantDias)+ " dias tranzados")

import datetime
ahora=datetime.datetime.now()
print (" Esta consulta se realiza en la fecha y hora" + " " + str (ahora) + " " + "Gracias por confiar en su asesor experto ingeniero Orlando Martinez")
