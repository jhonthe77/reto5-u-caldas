
def menu():
    print("********************* BIEMBENIDO************************")
    print("si es un usuario nuevo ingrese el numero (1)")
    print("si es un usuario existente ingrese el numero (2)")
    print("para salir ingrese el numero (3)")
    respuesta = input("Ingrese su eleccion: ")
    if respuesta=='1'or respuesta=='2':
        return int(respuesta)
    elif respuesta=='3':
        exit()
    else:
        print("varlor invalido")
        menu()






