def user_new(res):
    if res==1:
        print("el usuario debe tener 10 caracteres y una @ en cualquier pocision")
        usuario = input("ingrese un usuario por favor: ")
        if len(usuario) == 10 and usuario.count('@') == 1:
            print("usuario valido:]")
            nombre = input("ingrese su nombre por favor: ")
            edad = input("ingrese su edad por favor: ")
            estracto = input("ingrese su estracto por favor: ")
            if edad.isdigit() and estracto.isdigit() and len(nombre)>0 :
              print(usuario,nombre,edad,estracto)
            else: print("datos invalidos")