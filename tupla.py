def Menu():
    """Funcion que Muestra el Menu"""
    print ("""************
    Calculadora
    ************
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir""")

def Calculadora():
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print ("La Suma es:", x+y)
            print("¿Desea realizar otra operacion? s/n")
            pt=input()
            if (pt == "s"):
                print ("""
                Calculadora
                -----------
                Menu
                1) Suma
                2) Resta
                3) Multiplicacion
                4) Division
                5) Salir""")
                opc = int(input("Selecione Opcion\n"))
            else:
                print("Muchas gracias")
                break
        elif(opc==2):
                print ("La Resta es:",x-y)
                print("¿Desea realizar otra operacion? s/n")
                pt=input()
                if (pt == "s"):
                    print ("""
                    Calculadora
                    -----------
                    Menu
                    1) Suma
                    2) Resta
                    3) Multiplicacion
                    4) Division
                    5) Salir""")
                    opc = int(input("Selecione Opcion\n"))
                else:
                    print("Muchas gracias")
                    break
        elif(opc==3):
                print ("La Multiplicacion es:",x*y)
                print("¿Desea realizar otra operacion? s/n")
                pt=input()
                if (pt == "s"):
                    print ("""
                    Calculadora
                    -----------
                    Menu
                    1) Suma
                    2) Resta
                    3) Multiplicacion
                    4) Division
                    5) Salir""")
                    opc = int(input("Selecione Opcion\n"))
                else:
                    print("Muchas gracias")
                    break
        elif(opc==4):
                print ("La Division es:", x/y)
                print("¿Desea realizar otra operacion? s/n")
                pt=input()
                if (pt == "s"):
                    print ("""
                    Calculadora
                    -----------
                    Menu
                    1) Suma
                    2) Resta
                    3) Multiplicacion
                    4) Division
                    5) Salir""")
                        
                    opc = int(input("Selecione Opcion\n"))
                else:
                    print("Muchas gracias")
                    break
Calculadora()
