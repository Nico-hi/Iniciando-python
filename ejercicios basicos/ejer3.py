set1={1,2,3,4,5}
set2={4,5,6,7,8}

setUnion = set1.union(set2)
print(setUnion," <- Union")

setInter = set1.intersection(set2)
print(setInter," <- Interseccion")

setDif = set1.difference(set2)
print(setDif," <- Diferencia")

set1.add(11)
print(set1," <- Añadir")

set2.remove(6)
print(set2," <- Añadir")