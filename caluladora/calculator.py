import Menu as m
# 1. Crea las opciones y el nombre del menú
print("Hello, this is my first calculator with python")
options=["addition","subtraction","multiplication","division"]
menu_name="My first calculator"
# 2. Crea una instancia (un objeto) de la clase Menu
# Aquí es donde se llama al __init__(self, options, name)
My_menu=m.Menu(menu_name,options)
# 3. Llama al método show_menu en la instancia (objeto) que acabas de crear
# Aquí, 'my_menu' es 'self' para el método show_menu
leave=False
while leave!=True:
    My_menu.show_menu()
    selected_option=My_menu.choose_option()
    print("------------------------------")
    print(f"seleccionaste la opcion:\n {selected_option}")
    first_num=None
    second_num=None
    if selected_option!=0:
        first_num=int(input("first number --> "))
        second_num=int(input("second number --> "))
    match selected_option: # este match es como un switch de java
        case 1:
            print("the result is -> ",first_num+second_num)
        case 2:
            print("the result is -> ",first_num-second_num)
        case 3:
            print("the result is -> ",first_num*second_num)
        case 4:
            print("the result is -> ",first_num/second_num)
        case 0:
            leave=True
            print("thank you for use my calculator")
