salir = False
alumnos = []
estados = ("suspenso","aprobado") # esto no lo veo necesario pero dice tupla... asique lo pongo aca 

def calcular_estadisticas():# el comentario de abajo seria mas corto pero para explicarlo un poco mejor, pero segundo parrafo no es necesario....
    """ 
    Calcula estadísticas sobre los alumnos almacenados en la lista.

    Returns: un diccionario con los siguientes elementos " clave : valor "
        total       :total -> retona el total de alumnos que hay en la lista
        aprobados   :aprobados -> retona el total de aprobados
        suspensos   :suspensos -> retona el total de desaprobados
        media       :media -> retona la media total de los alumnos
    """
    total = 0
    aprobados = 0
    suspensos = 0
    media = 0 
    for alumno in alumnos:
        total=total+1
        if alumno['estado'] == "aprobado" : # esto no sabria como hacerlo sin el == porque otra forma creo que no es posible
            aprobados=aprobados+1 # forma contradida el aprobados+=1
        else:
            suspensos=suspensos+1
        media = media + alumno['nota']# tambien se puede poner en su forma contraida
    if total > 0 : media = media/total #se podria poner el "total != 0" pero no se si estaria bien... porque no lo veo en los apuntes
    return {
        "total":total,
        "aprobados":aprobados,
        "suspensos":suspensos,
        "media":media
    }

while not salir: # o tambien lo puedo poner como salir == False
    try:# el \n lo usamos como un salto de linea, se explico en clases....
        print('------------------------------\nMenu Examen Python\n------------------------------\n  1.- añadir alumnos\n  2.- listar alumnos\n  3.- ver estadisticas\n  0.- salir')
        option = int(input('------------------------------\nelija una opcion --> '))
        match option :
            case 1:
                print('------------------------------')
                nombre = input('ingrese su nombre --> ')
                while True: #iniciamos un segundo bucle para la excepcion de la nota
                    try:
                        nota = float(input('ingrese la nota del 0 al 10 --> '))
                        if (nota >=0 and nota <=10 ):
                            #en vez de hacer esto ...
                            #estado = "suspenso"
                            #if (nota>=5): estado = "aprobado"
                            #hare esto.... porque guardamos los datos en una tupla al inicio
                            estado = estados[0] # definimos su valor inicial como suspenso
                            if (nota>=5): estado = estados[1] # esto lo puse junto porque se hace mas corto, tambien puede ir separado...
                            alumnos.append({"nombre":nombre, "nota":nota, "estado":estado})
                            break
                        else:
                            print('>> dicha nota no esta en el rango estipulado, ingrese algo valido <<')
                    except ValueError:
                        print('>> tienes que poner un nuemro, intenta de nuevo. <<')
            case 2:
                if not alumnos : #tambien se puede poner el "" if (alumnos == []) "" pero para que sea mas legible lo comparamos con una lista vacia con el [] 
                    print('>> La lista esta vacia, por favor ingrese un alumno... <<')
                else:
                    print('------------------------------')
                    for alumno in alumnos:
                        print(f"Nombre : {alumno['nombre']}\nNota : {alumno['nota']}\nEstado : {alumno['estado']}\n__--__--__--__")
            case 3:
                estadisticas = calcular_estadisticas()
                print('------------------------------')
                print(f'Total de alumnos : {estadisticas['total']}\nTotal de aprobados : {estadisticas['aprobados']}\nTotal de suspensos : {estadisticas['suspensos']}\nMedia total : {estadisticas['media']}')
            case 0:
                salir = True # esto va por si no tenemos el break abajo, pero como hay dicho break nos sirve para salir directo.... "esto seria la forma para salir del programa si no hay break "
                print('------------------------------')
                print('Gracias por usar mi programa')
                break
    except ValueError :
        print('>> Escribiste algo distinto a un numero, intenta de nuevo. <<')
        