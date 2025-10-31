import Menu as m
options=["Calcular margen","Calcular descuento"]

leave = False
menu=m.Menu("... elije una opcion ...",options)
while leave == False :
    menu.show_menu()
    select_option = menu.choose_option()

    match select_option :
        case 1:
            num1 =input("dime el precio -> ")
            num2 =input("dime el margen en numero entero ->")
            margen = float(num1)/(1-(float(num2)/100))
            print(f"El precio es de {num1}\nEl margen que buscas es {num2}\nEl margen es {margen}")
        case 2:
            num1 =input("dime el precio -> ")
            num2 =input("dime el descuento en numero entero ->")
            descuento = float(num1)*(float(num2)/100)
            print(f"El precio es de {num1}\nEl descuento que buscas es {num2}\nEl descuento es que tiene el producto es {descuento}%")
        case 0:
            leave = True
