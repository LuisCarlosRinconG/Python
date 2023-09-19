while(True):
    print("DIGITA LOS VALORES A ENCRIPTAR: ")
    a = float(input("\nDigita el valor de a \n"))
    b = float(input("Digita el valor de b \n"))
    c = float(input("Digita el valor de c \n"))

    if(a==0 or b==0):
        print("\nLos numeros no pueden ser cero")
        break
    
    
    opcion=input("\n¿Que desea hacer? \n1)Encriptar mensaje \n2)Desencriptar mensaje \n3)Salir\n")
    
    if(opcion == "1"):
        pedir = float(input("\nCual es tu mensaje para encriptar\n"))
        if(pedir==0):
            print("El mensaje no puede ser cero")
            break
        encriptar = (((pedir*a)/b)+c)
        print("\nTu mensaje encriptado es: \n")
        print(encriptar)
    elif(opcion == "2"):
        pedir2 = float(input("\nCual es tu mensaje para desencriptar: \n"))
        if(pedir2==0):
            print("El mensaje no puede ser cero")
            break
        desencriptar = (((pedir2-c)*b)/a)
        print("\nTu mensaje desencriptado es: \n")
        print(desencriptar)
    elif(opcion == "3"):
        break
    else:
        print("\nDigistaste una opcion incorrecta")
