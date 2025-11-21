inventario = {}
salir = True
while salir == True :
    print("---------------------------------------")
    print("Bienvenido al sistema de gestion de inventario")
    print("---------------------------------------")
    print("1. Añadir producto")
    print("2. consultar inventario")
    print("3. actulizar cantidad de producto'")
    print("0. Salir")
    print("---------------------------------------")

    opcion = input("Seleccione una opcion : ")
    print("---------------------------------------")
    print("---------------------------------------")

    
    if opcion == "1":
        # Lógica para agregar producto
        print("Agregar producto seleccionado")
        nombre_producto = input(">> Ingrese el nombre del producto: ")
        if nombre_producto in inventario:
            print(">>>> El producto "+inventario[nombre_producto] + " ya existe en el inventario.")
        else:
            cantidad_producto = input(">> Ingrese la cantidad del producto: ")
            if cantidad_producto.isdigit():
                cantidad_producto = int(cantidad_producto)
                inventario[nombre_producto] = cantidad_producto
                print(">>>> Producto " + nombre_producto + " agregado con cantidad " + str(cantidad_producto))
            else:
                print(">>>> Cantidad invalida, por favor ingrese un numero.")
    elif opcion == "2":
        if inventario == {}:
            print(">>>> El inventario esta vacio.")
        else:
            print(">> Inventario actual:")
            for producto, cantidad in inventario.items():
                print(f">>>> {producto}: {cantidad}")
    elif opcion == "3":
        print("Actualizar cantidad de producto seleccionado")
        nombre_producto = input(">> Ingrese el nombre del producto a actualizar: ")
        if nombre_producto in inventario:
            nueva_cantidad = input(">> Ingrese la nueva cantidad del producto: ")
            if nueva_cantidad.isdigit() and int(nueva_cantidad) >= 0:
                nueva_cantidad = int(nueva_cantidad)
                inventario[nombre_producto] = nueva_cantidad
                print(">>>> Cantidad del producto actualizada")
            else:
                print(">>>> Error no ha suficiente cantidad en el inventario.")
        else:
            print(">>>> El producto no existe en el inventario.")
    elif opcion == "0":
        salir = False
        print("Saliendo del sistema de gestion de inventario")
    else:
        print("Opcion no valida, por favor intente de nuevo.")