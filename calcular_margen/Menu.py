class Menu: # aqui estoy iniciando una clase ...
    def __init__(self, name,options):
        # Se acepta list, tuple, o set para 'opciones', luego se convierte a list.
        if not isinstance(options, (list, tuple, set)):
            raise TypeError("Las opciones del menú deben ser una lista, tupla o conjunto.")
        # Validaciones de tipo mejoradas para ser más claras
        if not isinstance(name, str):
            raise TypeError("El título del menú debe ser una cadena de texto.")
        
        self.options=list(options)
        self.name=name
        self.opcion_elegida = -1

    def show_menu(self):
        i=0
        print(f"---------{self.name}---")
        print("------------------------------")
        while i<len(self.options):     
            print(f"{i+1}.-{self.options[i]}")
            i+=1
        print("0.- leave")       
        print("------------------------------")
        print("choose an option")

# """
# """ --> this is a option to comment with more code lines
#def show_menu(self):
#    for i, option in enumerate(self.options, start=1):
#        print(f"{i}.- {option}")
#    print("Choose an option")
#    return self.choose_option()
#
#
    def choose_option(self):
        while True:
            try:
                option=int(input("-->"))
                if 0 <= option and option <= len(self.options):
                    return option
                else:
                    print(f"you just have {len(self.options)} options, between 0 to {len(self.options)} ")
            except ValueError:
                print(f"You have to write a number between 1 to {len(self.options)} ")


