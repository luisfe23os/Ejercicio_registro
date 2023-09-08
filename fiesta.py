print("Fiesta crazy")
print("**********")
print("0.salir")
print("1.registrar invitado")
print("2.ver lista de invitados")
print("3.ver quien pago ")
print("4.ver quien no pago")
print("5.cambiar informacion eps")
print("6.retirar invitados")
print("**********")

opcion = 8
invitados = []
id = 0
while opcion != 0:
    invitado = {}
    encontrado = False
    opcion = int(input("ingrese un numero "))
    if opcion == 1:
        id += 1
        invitado["nombre"] = input("digite su nombre ")
        invitado["id"] = id
        invitado["cedula"] = input("ingrese su cedula ")
        invitado["eps"] = input("dgite su eps ")
        invitado["edad"] = input("edad ")
        invitado["estado"] = input(
            "1-> pago o 2-> no pago "
        )  # invitado["estado"]=bool(input("pago?? "))
        invitado["valorcouta"] = float(input("ingrese el valor de la couta "))  # casteo

        invitados.append(invitado)

    elif opcion == 2:
        # pass passar al siguiete
        # recorrido de la lista
        # print(invitados)
        for persona in invitados:
            print(f"persona:{persona['id']},{persona['nombre']}")
            #print(f"persona:{persona['id']}")
    elif opcion == 3:
        for persona in invitados:
            if persona["estado"] == "1":
                print("usuarios que pagaron la couta")
                print(f"persona:{persona['id']},{persona['nombre']}")
            else:
                print(" para ver quienes no han pagado selecione opcion 4")
    elif opcion == 4:
        for persona in invitados:
            if persona["estado"] != "1":
                print("Usuarios que no han pagado")
                print(f"persona:{persona['id']},{persona['nombre']}")
            else:
                print("aun no hay usuarios que no hayan pagado")    
    elif opcion == 5:
            id_invitado = int(input("Ingrese el ID del invitado cuya EPS desea cambiar: "))

            for invitado in invitados:
                if invitado["id"] == id_invitado:
                    nueva_eps = input("Ingrese la nueva EPS: ")
                    invitado["eps"] = nueva_eps
                    print("Se actualizó la información de EPS.")
                    encontrado = True
                    break

            if not encontrado:
                print("No se encontró un invitado con ese ID.")

    elif opcion == 6:
        id_invitado = int(input("Ingrese el ID del invitado para eliminar: "))
        encontrado = False

        for invitado in invitados:
            if invitado["id"] == id_invitado:
                invitados.remove(invitado)
                print("Se ha eliminado al invitado.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un invitado con ese ID.")

    else:
     print("opcion invalidad")
