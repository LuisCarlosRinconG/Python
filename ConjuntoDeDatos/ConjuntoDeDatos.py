
# Importar libreria matplotlib
import matplotlib.pyplot as plt
# Solicita el nombre y crear variables a utilizar
Nombre = input("Cual es tu nombre")
Etiquetas = ["Cantidad de fresas","Cantidad de fresas \n de primera calidad "]
Terminar = 0
while(True):
 #Menu de usuario
 opcion = input("¿Que desea realizar el día de hoy señor " + Nombre +"? \n 1) Ingresar información \n 2) Buscar información por zona o fecha \n 3) Graf
 
 if(opcion == "1"):
 print("Decidiste ingresar información")
 fecha = input("Ingresa la fecha de registro: ")
 zona = input("Ingresa la zona: ")
 cantidad = input("Que cantidad de fresa se recogio en libras: ")
 ccantidad = input("Que cantidad de fresas de primera calidad se recogio en libras: ")
 
 if(zona == "1"):
 variable = open("Zona Uno","w")
 variable.write("\n La fecha de el registro es: "+ fecha +"\n La zona es: "+ zona + "\n La cantidad de fresa es: " + cantidad + " lbs, \n la ca
 variable.close()
 f1 = fecha
 z1 = [cantidad,ccantidad]
 elif(zona == "2"):
 variable = open("Zona Dos","w")
 variable.write("\n La fecha de el registro es: "+ fecha +"\n La zona es: "+ zona + "\n La cantidad de fresa es: " + cantidad + " lbs, \n la ca
 variable.close()
 f2 = fecha
 z2 = [cantidad,ccantidad]
 elif(zona == "3"):
 variable = open("Zona Tres","w")
 variable.write("\n La fecha de el registro es: "+ fecha +"\n La zona es: "+ zona + "\n La cantidad de fresa es: " + cantidad + " lbs, \n la ca
 variable.close()
 f3 = fecha
 z3 = [cantidad,ccantidad]
 elif(zona == "4"):
 variable = open("Zona cuatro","w")
 variable.write("\n La fecha de el registro es: "+ fecha +"\n La zona es: "+ zona + "\n La cantidad de fresa es: " + cantidad + " lbs, \n La ca
 variable.close()
 f4 = fecha
 z4 = [cantidad,ccantidad]
 else:
 print("\n No existe ninguna zona con este numero para almacenar los datos")
 
 elif(opcion == "2"):
 buscar = input("¿Desea buscar los datos por \n1)Fecha \no \n2)Zona?\n")
 if(buscar == "1"):
 InFecha = input("¿Cual es la fecha que buscas?")
 if(InFecha == f1):
 print("\n La fecha de el registro es: "+ f1 +"\n La zona es: zona 1 \n La cantidad de fresa es: " + z1[0] + " lbs, \n La cantidad de fresa
 if(InFecha == f2):
 print("\n La fecha de el registro es: "+ f2 +"\n La zona es: zona 2 \n La cantidad de fresa es: " + z2[0] + " lbs, \n La cantidad de fresa
 if(InFecha == f3):
 print("\n La fecha de el registro es: "+ f3 +"\n La zona es: zona 3 \n La cantidad de fresa es: " + z3[0] + " lbs, \n La cantidad de fresa
 if(InFecha == f4):
 print("\n La fecha de el registro es: "+ f4 +"\n La zona es: zona 4 \n La cantidad de fresa es: " + z4[0] + " lbs, \n La cantidad de fresa
 else:
 print("La fecha no se encuentra")
 elif(buscar=="2"):
 IZona=input("¿Que zona es la que buscas?")
 if(IZona=="1"):
 print("\n La fecha de el registro es: "+ f1 +"\n La zona es: zona 1 \n La cantidad de fresa es: " + z1[0] + " lbs, \n La cantidad de fresa
 elif(IZona=="2"):
 print("\n La fecha de el registro es: "+ f2 +"\n La zona es: zona 2 \n La cantidad de fresa es: " + z2[0] + " lbs, \n La cantidad de fresa
 elif(IZona=="3"):
 print("\n La fecha de el registro es: "+ f3 +"\n La zona es: zona 3 \n La cantidad de fresa es: " + z3[0] + " lbs, \n La cantidad de fresa
 elif(IZona=="4"):
 print("\n La fecha de el registro es: "+ f4 +"\n La zona es: zona 4 \n La cantidad de fresa es: " + z4[0] + " lbs, \n La cantidad de fresa
 else:
 print("La zona no se encuentra")
 Terminar = 1
 
 elif(opcion == "3"):
 print("Graficar")
 graficar = input("¿Que zona deseas graficar?")
 
 if (graficar == "1"):
 fig,ax = plt.subplots()
 ax.pie(z1, labels = Etiquetas, autopct = "%0.1f %%",
 pctdistance = 0.4, labeldistance = .6)
 ax.set_title("Grafico del cultivo de la zona Uno")
 plt.show()
 elif(graficar == "2"):
 fig,ax = plt.subplots()
 ax.pie(z2, labels = Etiquetas, autopct = "%0.1f %%",
 pctdistance = 0.4, labeldistance = .6)
 ax.set_title("Grafico del cultivo de la zona Dos")
 plt.show()
 elif(graficar == "3"):
 fig,ax = plt.subplots()
 ax.pie(z3, labels = Etiquetas, autopct = "%0.1f %%",
 pctdistance = 0.4, labeldistance = .6)
 ax.set_title("Grafico del cultivo de la zona Tres")
 plt.show()
 elif(graficar == "4"):
 fig,ax=plt.subplots()
 ax.pie(z4, labels=Etiquetas, autopct="%0.1f %%",
 pctdistance = 0.4, labeldistance=.6)
 ax.set_title("Grafico del cultivo de la zona Cuatro")
 plt.show()
 
 elif(opcion == "4"):
 print("Gracias y hasta pronto")
 break
 
 else:
 print("ERROR DE DIGITACIÓN")
