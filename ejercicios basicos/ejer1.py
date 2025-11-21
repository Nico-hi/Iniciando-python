def PrintList(list):
    print(len(list),'<- longitud del array/list')
    for elemnt in list:
        print(elemnt)

names = ['carlos','jose','alonzo','michael','no se que mas nobres poner xD']
print('---------------apartado 1 ------------')
PrintList(names)
print('---------------apartado 2 ------------')
print(f"{names[2]}este es el segundo nombre de la lista de nombre, si quieres sacarlo puedes hacerlo mediante:\n names[#], donde # es el numero de la lista empezando por 0")
print('---------------apartado 3 ------------')
names[2] ='nuevo nombre'
PrintList(names)
print('---------------apartado 4 ------------')
names.append("un nombre mas largo del que se suele usar")
PrintList(names)
print('---------------apartado 5 ------------')
names.pop(len(names)-1)
PrintList(names)
