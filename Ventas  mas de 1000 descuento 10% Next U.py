NombreC= input("Ingese su nombre " )
comprasC= input("Ingrese el nombre del producto " )
valor=float(input("Ingrese el valor del producto " ))
if valor<=0:
    input ("Por favor ingrese numero mayor a cero")
cantidad = float(input("Ingrese la cantidad del producto " ))
if cantidad<=0:
    input ("Por favor ingrese numero mayor a cero")
valorTotal = valor*cantidad
if valorTotal>=1000:
   valorTotal*0.1
input ("El total a pagar es de con el 10% de descuento " + str(valorTotal))
