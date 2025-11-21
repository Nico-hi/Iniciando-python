def PrintDic(dict):
    print(len(dict))
    for key in dict:
        print(f'" {key} " es la clave y " {dict[key]} " es su valor correspondiente \n')

info_student = {
    'nombre':'nicolas',
    'edad':19,
    'asignaturas':['python','php','java']
}
print('---------------diccionario completo ------------')
PrintDic(info_student)
print('---------------apartado 1 ------------')
print(f'el nombre del diccionario es {info_student['nombre']}, con la sentencia info_student["nombre"]')
print('---------------apartado 2 ------------')
info_student['asignaturas'].append('js')
print(f'anadimos js con el comando info_student["asignaturas"].append("js") ')
print(info_student['asignaturas'])
print('---------------apartado 3 ------------')
info_student['edad']=777
print('info_student["edad"]=777')
print('---------------apartado 4 ------------')
info_student['asignaturas'].pop(0)
print('info_student.pop(0)')

print('--------------- resultados ------------')
PrintDic(info_student)
