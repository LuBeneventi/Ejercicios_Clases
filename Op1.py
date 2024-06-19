elegido = False
asientos = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
while True:
    print("---------------------")
    print("1. Reserva")
    print("2. Asientos disponibles")
    print("3. Salir")
    print("---------------------")
    op = input("Ingrese la opción a realizar: ")
    if op == "1":
        while True:
            rut = input("Ingrese su rut: ")
            if len(rut) != 9:
                continue
            else:
                break
        print("Asientos disponibles:")
        for i in range(len(asientos)):
            print(asientos[i])
        while True:
            opcion_asiento = input("¿Asiento de ventana o pasillo?(v/p): ")
            if opcion_asiento == "v" and elegido == False:
                for i in range(len(asientos)):
                        if asientos[i][0] == 0:
                            asientos[i][0] = "X"
                            elegido = True
                        elif asientos[i][3] == 0 and elegido == False:
                            asientos[i][3] = "X"
                            elegido = True
                        else: 
                            print("No hay asientos de ventana disponibles")
            elif opcion_asiento == "p":
                for i in range(len(asientos)):
                        if asientos[i][1] == 0 and elegido == False:
                            asientos[i][1] = "X"
                            elegido = True
                        elif asientos[i][2] == 0 and elegido == False:
                            asientos[i][2] = "X"
                            elegido = True
                        else: 
                            print("No hay asientos de ventana disponibles")
                            elegido = False
            else:
                print("Opción no valida")
            if elegido == True:
                break
            else:
                continue


