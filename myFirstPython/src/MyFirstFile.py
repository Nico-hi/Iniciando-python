print("Hello")
salir = True
var1 = 1
var2 = 'a'
var3 = "Este es un String"
var4 = 12,3 # numero entero (int) siendo alma
var5 = 302.3 # numero decimal (float)
var6 = None # valor nulo
var10=2+3j # numero complejo
var11=13.e3 # numero en notacion cientifica
var_1=(1,2,3,"ffds")#tuplas --Inmutable --Datos fijos, retornos múltiples de funciones.
var_2=["132",213,"gd"]#listas --Mutable-- Colecciones ordenadas de elementos cambiantes.
var_3={1, 2, 3}# set --Colecciones sin duplicados, operaciones de conjunto.
var_4={"a": 1, "b": 2}# dict --Mapeo clave-valor, estructuras asociativas.


# esto es igual que js con un "+" es para concatenar cadenas de string puras
#pero para juntarlo con distintos tipos de datos se usa el ","
#Convierte  a texto usando str(): ----- mejor aún, usa f-strings (más legibles):
print("-----------------------------------------------------")
print(salir,"--> es de tipo -->",type(salir))
print(var1,"--> es de tipo -->",type(var1))
print(var2,"--> es de tipo -->",type(var2))
print(var3,"--> es de tipo -->",type(var3))
print(var4,"--> es de tipo -->",type(var4))
print(var5,"--> es de tipo -->",type(var5))
print(var6,"--> es de tipo -->",type(var6))
# aca estamos viendo la variable y que tipo es
print(var_1,"--> es de tipo -->",type(var_1))
print(var_2,"--> es de tipo -->",type(var_2))
print(var_3,"--> es de tipo -->",type(var_3))
print(var_4,"--> es de tipo -->",type(var_4))
print("------------- aca puedes imprimir elementos de los 4 anteriores valores -----------")
print("el primer valor de var_1 -> lo ponemos como var_1[#] -->",var_1[1])
print("el primer valor de var_2 -> lo ponemos como var_2[#] -->",var_2[1])
var_3_1=list(var_3)
print("el primer valor de var_3 -> lo ponemos como var_3[#] no podemos hacerlo de esa formantenemos que convertirlo \en una lista para poder sacar el elemnto -->",var_3_1[1])
print("el primer valor de var_4 -> lo ponemos como var_4[#] , el # es la clave (tomamos como referenica el HashMap de java) -->",var_4['a'])
print("--------------------------------------------------------")
#tomamos estos conceptos basicos para las litas
print("esta es la lista original",var_2)
var_2[0]='otro texto'# hacemos el cambio de dato en el elemnto que queremos
print("hemos cambiado el valor de la primera posicion\n",var_2)
var_2.append('nombre_ejemplo')# esto nos añadiora el elemento al final la lista
print("anadimos en valor con append\n",var_2)
var_2.insert(3,214423)# aca ponemos el incide o la posicion en la que queremos poner un dato
print("ponemos el dato en la posicion 4 (siempre se empieza desde el 0)\n",var_2)
var_2.remove("gd")
print("eliminamos el valor gd\n",var_2,"sacamos la posicion del valor 213\n",var_2.index(213),"\nsacamos la longitud de la lista\n",len(var_2))
#en aca podemos ver como asiganar valores a varios elementos en una sola linea
#tiene que ser en si posicion respectiva, si tenen mas o menos en cualquier lado salta error
print("-----------------------------------------------------")
var7,var8,var9=123,"Hello",(21,"sfa",'s')
print(var7,"||",var8,"||",var9,"--> son de tipo -->",type(var7),"||",type(var8),"||",type(var9),"respectivamenye")
    # aqui tenemos distintas formas de asignar valores, pueden mutar los valores
a1,b1,c1=1,1,1
#ejemplo
print(a1,"--> es de tipo -->",type(a1))# aqui el valor de a1 es un int
a1="Hello"
print(a1,"--> es de tipo -->",type(a1))# aca se converte en un string
a2=1
b2=1
c2=1
a3=b3=c3=1
print("-----------------------------------------------------")



#Block Indentation
# That is, blocks in Python, such as functions, loops, if clauses and other constructs, have no ending identifiers. All blocks start with a
#  colon and then contain the indented lines below it.
print("aca ingresaremos a la funcion")
def my_funtion():# aqui definimos una funcion poniendo como inicio el ":"
    d1="valor"   # al tener la definicion o uno de ls ejemplos anteriores nos da una tabulacion la cual nos indica que estamos dentro
    return d1   #aca escribimos return ( como en java para saber que la clase termina en ese punto)
# al salir de la funcion volvemos al codigo original que nos permite hacer cosas fuera de dicha clase/definicion/funcion
print("este es imprimiendo directamente el nombre de la funcion\n",my_funtion) # aca imprimimos que tipo es, su nombre y la direccion de memoria
# para ejecutarla debems hacer esto
d1=my_funtion() # a una variable debemos ponerle de variable para guardar el resultado
print("esto es cuando pasamos la funcion a una variable y dicha variable lo imprimimos\n",d1)
