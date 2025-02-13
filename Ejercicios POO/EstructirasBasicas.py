#--------No hay que declarar variables
print(3+2)
n=4
print(n)
nota1=5
nota2=6
notaMedia=(nota1+nota2)/2
print(notaMedia)
#------Cadenas, las cadenas se puede poner entre comillas simples o dobles.----------
'Hola mundo'
"Hola Mundo"
'Esta \"palabra\" va entre comillas'
'\t indica alineación'
'\n Salto de linea'
print('Esta \"cadena\" va entre comillas')
print('Una linea \n otra linea')
cadena="Hola "
print(cadena*2)
cadena1="Hola"
cadena2="mundo"
print(cadena1+" "+cadena2)
espacio=" "
print("Esto son diez espacios:"+(espacio*10)+".")
#Posiciones en cadenas
palabra="Python"
print(palabra[1])
print(palabra[-1])
print(palabra[0:2])
#-------LISTAS-----
numeros=[1,2,3,4,5]
print(numeros)
datos=["Hola",1,"4",10," esto es una cadena ", "3",4," esto es otra"]

#----FUNCIONES----
print(len(datos))
print(datos[1])
print(datos[len(datos)-1])
print(datos[0:2])
print(numeros+[6,7,8,9])
pares=[2,4,5,8,10]
pares[2]=6
print(pares)
pares.append(12)
print(pares)
letras=['a','b','c','d','f']
print(letras[0:3])
print(letras[:3])
letras[0:3]=['A','B','C']
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
r=[a,b,c]
print(r[1])
print(r[1][1])
print(r[-1])
print(r[-1][-1])
#-----BOOLEANS-------
print(1+1==3)
print(1+1==2)
#Las cadenas se comparan con ==
print(cadena==cadena1)
print(3>2)
print(3!=2)
a=10
b=5
print(a==b*2)
print("Hola"=="Hola")
print(a==b)
print(len(a)==len(b))
print(True*3)#True vale 1
print(False*3)#False vale 0
print(True and True)
print(False and True)
print(False or True)
c="Hola Mundo"
print(len(c)>=20 and c[0]=='H')
print(len(c)>=20 or c[0]=='H')
c="Lectura"
print(c[0]=='H' or c[0]=='h')
#----OPERACIONES MATEMATICAS----
a=5
a+=2
print(a)
#------Sistema de flujo-----




