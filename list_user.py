def list_user(res):
    lista1 = ['elpillo@pl', 'jhorman', 24, 4]
    lista2 = ['cangri@cgk', 'iroman', 27, 3]
    lista3 = ['jhonwick@k', 'jhon', 29, 5]
    usuarios = {'user1': lista1, 'user2': lista2, 'user3': lista3}
    nobres = ['']
    contador = 0
    for i in usuarios:
        contador += 1
        nobres.append(usuarios[i][1])
        n = usuarios[i][1]
        print(contador, n)
    respuesta = input("ingrese el numero de su usuario: ")
    if respuesta.isdigit() and res==2:
        respuesta = int(respuesta)
        if respuesta > 0 and respuesta <= 3 and respuesta <= len(nobres) :
            print("Bienbenido", nobres[respuesta])
            print("que datos desea cambiar: ")
            print("(1) para la edad \n(2) para el estracto \n(3) el usuario")
            modificar = input("ingresa tu respuesta: ")
            lis = [modificar == '1' and respuesta == 1, modificar == '2' and respuesta == 1,
                   modificar == '3' and respuesta == 1]
            lis1 = [modificar == '1' and respuesta == 2, modificar == '2' and respuesta == 2,
                    modificar == '3' and respuesta == 2]
            lis2 = [modificar == '1' and respuesta == 3, modificar == '2' and respuesta == 3,
                    modificar == '3' and respuesta == 3]

            for k in lis:
                if lis[0]:
                    edad = int(input("ingrese su edad por favor: "))
                    usuarios['user1'][2] = edad
                    print(usuarios['user1'])
                    break
                elif lis[1]:
                    estracto = int(input("ingrese su estracto por favor: "))
                    usuarios['user1'][3] = estracto
                    print(usuarios['user1'])
                    break
                elif lis[2]:
                    usuario = input("ingrese un usuario por favor: ")
                    if len(usuario) == 10 and usuario.count('@') == 1:
                        usuarios['user1'][0] = usuario
                        print(usuarios['user1'])
                    break

            for k in lis1:
                if lis1[0]:
                    edad = int(input("ingrese su edad por favor: "))
                    usuarios['user2'][2] = edad
                    print(usuarios['user2'])
                    break
                elif lis1[1]:
                    estracto = int(input("ingrese su estracto por favor: "))
                    usuarios['user2'][3] = estracto
                    print(usuarios['user2'])
                    break
                elif lis1[2]:
                    usuario = input("ingrese un usuario por favor: ")
                    if len(usuario) == 10 and usuario.count('@') == 1:
                        usuarios['user2'][0] = usuario
                        print(usuarios['user2'])
                    break

            for k in lis2:
                if lis2[0]:
                    edad = int(input("ingrese su edad por favor: "))
                    usuarios['user3'][2] = edad
                    print(usuarios['user3'])
                    break
                elif lis2[1]:
                    estracto = int(input("ingrese su estracto por favor: "))
                    usuarios['user3'][3] = estracto
                    print(usuarios['user3'])
                    break
                elif lis2[2]:
                    usuario = input("ingrese un usuario por favor: ")
                    if len(usuario) == 10 and usuario.count('@') == 1:
                        usuarios['user3'][0] = usuario
                        print(usuarios['user3'])
                    break
        else:
            print("varlor invalido")
            list_user(res)


    else:
        print("varlor invalido")
        list_user(res)